#!/usr/bin/python
# -*- coding: utf-8 -*-

from HTTPRequest import HTTPRequest
from email.utils import formatdate
from twisted.internet import error
from twisted.protocols.basic import LineReceiver
from twisted.python import failure
import OpenSSL
import biplist
import logging
import struct
import threading
import zlib
import pprint

class Ping(object):
    def __init__(self, num):
        self.num = num
        
class ServerObject(object):
    def __init__(self, plist):
        self.plist = plist

class Siri(LineReceiver):

    def __init__(self, server, peer):
        self.server = server
        self.peer = peer
        self.header = ""
        self.rawData = ""
        self.output_buffer = ""
        self.unzipped_output_buffer = ""
        self.unzipped_input = ""
        self.consumed_ace = False
        self.decompressor = zlib.decompressobj()
        self.compressor = zlib.compressobj()
        self.logger = logging.getLogger()
        self.sendLock = threading.Lock()

    def connectionMade(self):
        self.logger.info("New connection from {0} on port {1}".format(self.peer.host, self.peer.port))
        self.server.numberOfConnections += 1
        self.logger.info("Currently {0} clients connected".format(self.server.numberOfConnections))

    def connectionLost(self, reason):
        if reason.type == OpenSSL.SSL.Error:
            self.logger.warning("SSL related error")
            self.logger.warning(reason.value)
        elif reason.type == error.ConnectionLost:
            self.logger.warning("Connection Lost: {0}".format(reason.value))
        elif reason.type == error.ConnectionDone:
            self.logger.info("Connection Closed: {0}".format(reason.value))
        else:
            self.logger.error("Connection Lost: {0}".format(reason))
        self.server.numberOfConnections -= 1
        self.logger.info("Currently {0} clients connected".format(self.server.numberOfConnections))
        self.server = None
        self.peer = None
        self.decompressor = None
        self.compressor = None
        self.sendLock = None
        
    def checkHeader(self):
        if "\r\n\r\n" in self.header:
            # end of header found, lets check it
            self.logger.debug("--------------HEADER START---------------")
            self.logger.debug(self.header)
            self.logger.debug("---------------HEADER END----------------")
            request = HTTPRequest(self.header)
            if request.error_code == None:
                if request.command != "ACE":
                    return (405, "Method Not Allowed")
                if request.path != "/ace":
                    return (404, "Not Found")
            else:
                return (request.error_code, request.error_message)
            return True
        else:
            return False
    
    def lineReceived(self, line):
        self.header += line + "\r\n"
        headerCheck = self.checkHeader();
        success = False
        if type(headerCheck) == bool:
            if (headerCheck):
                code = 200
                message = "OK"
                success = True
            else:
                # we need to receive more
                return
        else:
            code, message = headerCheck
            
        self.output_buffer = ("HTTP/1.1 {0} {1}\r\nServer: Apache-Coyote/1.1\r\nDate: " + formatdate(timeval=None, localtime=False, usegmt=True) + "\r\nConnection: close\r\n\r\n").format(code, message)
        self.flush_output_buffer()
        if not success:
            self.transport.loseConnection()
        else:
            self.consumed_ace = False
            self.setRawMode()
        
    def rawDataReceived(self, data):
        self.rawData += data
        if not self.consumed_ace:
            if len(self.rawData) > 4:
                ace = self.rawData[:4]
                if ace != "\xaa\xcc\xee\x02":
                    self.output_buffer = "No stream start instruction found"
                    self.flush_output_buffer()
                    self.transport.loseConnection(failure.Failure(error.ConnectionDone('Other side is not conform to protocol.')))
                else:
                    self.output_buffer = "\xaa\xcc\xee\x02"
                    self.flush_output_buffer()
                self.rawData = self.rawData[4:]
                self.consumed_ace = True
            else:
                return
        self.process_compressed_data()
    
    def process_compressed_data(self):
        self.unzipped_input += self.decompressor.decompress(self.rawData)
        self.rawData = ""
        while self.hasNextObj():
            obj = self.read_next_object_from_unzipped()
            if type(obj) == Ping:
                self.received_ping(obj.num)
            if type(obj) == ServerObject:
                plist = biplist.readPlistFromString(obj.plist)
                self.received_plist(plist)
    
    def hasNextObj(self):
        if len(self.unzipped_input) == 0:
            return False
        if len(self.unzipped_input) < 5:
            return False
        
        cmd, data = struct.unpack('>BI', self.unzipped_input[:5])        
            
        if cmd in (3, 4): #ping pong
            return True
        if cmd == 2:
            return (len(self.unzipped_input) >= (data + 5))
    
    def read_next_object_from_unzipped(self):
        cmd, data = struct.unpack('>BI', self.unzipped_input[:5])
        if cmd == 3: #ping
            self.unzipped_input = self.unzipped_input[5:]
            return Ping(data)

        object_size = data
        object_data = self.unzipped_input[5:object_size + 5]
        self.unzipped_input = self.unzipped_input[object_size + 5:]
        return ServerObject(object_data)
    
    def send_object(self, obj):
        self.send_plist(obj.to_plist())

    def send_plist(self, plist):
        self.sendLock.acquire()
        self.logger.debug("Sending packet with class: {0}".format(plist['class']))
        self.logger.debug("packet with content:\n{0}".format(pprint.pformat(plist, width=40)))
        bplist = biplist.writePlistToString(plist);
        self.unzipped_output_buffer = struct.pack('>BI', 2, len(bplist)) + bplist
        self.flush_unzipped_output() 
        self.sendLock.release()
    
    def send_pong(self, idOfPong):
        self.sendLock.acquire()
        self.unzipped_output_buffer = struct.pack('>BI', 4, idOfPong)
        self.flush_unzipped_output() 
        self.sendLock.release()

    def flush_unzipped_output(self):
        self.output_buffer += self.compressor.compress(self.unzipped_output_buffer)
        #make sure everything is compressed
        self.output_buffer += self.compressor.flush(zlib.Z_SYNC_FLUSH)
        self.unzipped_output_buffer = ""
        self.flush_output_buffer()
        
    def flush_output_buffer(self):
        if len(self.output_buffer) > 0:
            self.transport.write(self.output_buffer)
            self.output_buffer = ""
 
