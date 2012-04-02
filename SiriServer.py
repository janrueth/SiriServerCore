#!/usr/bin/python
# -*- coding: utf-8 -*-
from SiriProtocolHandler import SiriProtocolHandler
from optparse import OptionParser
from os.path import exists
from socket import gethostname
from twisted.internet.protocol import Protocol
import PluginManager
import db
import logging
import sys


try:    
    from twisted.internet import ssl
    from twisted.internet.protocol import Factory
except ImportError:
    print "You need to install the twisted python libraries (http://twistedmatrix.com/trac/)\n"
    print "On a debian based system try installing python-twisted\n"
    print "On other systems, you may use easy_install or other package managers\n"
    print "Please refer to the website listed above for further installation instructions\n"
    exit(-1)
    
    
try:       
    from OpenSSL import crypto
except:
    print "You need to install the python OpenSSL module (http://packages.python.org/pyOpenSSL/openssl.html)\n"
    print "On a debian based system try installing python-openssl\n"
    print "On other systems, you may use easy_install or a package manager available there\n"
    print "Please refer to the website listed above for further installation instructions\n"
    exit(-1)
    


log_levels = {'debug':logging.DEBUG,
              'info':logging.INFO,
              'warning':logging.WARNING,
              'error':logging.ERROR,
              'critical':logging.CRITICAL
              }
       
class RejectHandler(Protocol):
    def makeConnection(self, transport):
        transport.loseConnection()
        return
    

class SiriFactory(Factory):

    def __init__(self, maxConnections):
        self.numberOfConnections = 0
        self.maxConnections = maxConnections
        self.sessionCert = None
        self.sessionCACert = None
        self.dbConnection = None
        
    def buildProtocol(self, addr):
        if self.maxConnections == None:
            return SiriProtocolHandler(self, addr)
        elif self.numberOfConnections < self.maxConnections:
            return SiriProtocolHandler(self, addr)
        else:
            return RejectHandler()
    
    def startFactory(self):
        logging.getLogger().info("Loading Session Certificates")
        caFile = open("keys/SessionCACert.pem")
        self.sessionCACert = crypto.load_certificate(crypto.FILETYPE_PEM,caFile.read())
        caFile.close()
        sessionCertFile = open("keys/SessionCert.pem")
        self.sessionCert = crypto.load_certificate(crypto.FILETYPE_PEM, sessionCertFile.read())
        sessionCertFile.close() 
        logging.getLogger().info("Setting Up Database")
        db.setup()
        logging.getLogger().info("Connection to Database")
        self.dbConnection = db.getConnection()
        logging.getLogger().info("Loading Plugin Framework")
        PluginManager.load_api_keys()
        PluginManager.load_plugins()
        logging.getLogger().info("Server is running and listening for connections")
        
    def stopFactory(self):
        logging.getLogger().info("Server is shutting down")
        self.dbConnection.close()
        logging.getLogger().info("Database Connection Closed")
        
        


ROOT_CA_CERT_FILE = "keys/ca.pem"
ROOT_CA_KEY_FILE = "keys/cakey.pem"
SERVER_CERT_FILE = "keys/server.crt"
SERVER_KEY_FILE = "keys/server.key"

def create_self_signed_cert():
    
    if not exists(SERVER_CERT_FILE) or not exists(SERVER_KEY_FILE) or not exists(ROOT_CA_CERT_FILE):

        print "I could not find valid certificates. I will now guide you through the process of creating some."
        
        print "I will create a Certification Authority (CA) first"
        # create a key pair
        ca_key = crypto.PKey()
        ca_key.generate_key(crypto.TYPE_RSA, 2048)

        # create a self-signed cert
        CAcert = crypto.X509()
        CAcert.get_subject().C = "DE"
        CAcert.get_subject().ST = "NRW"
        CAcert.get_subject().L = "Aachen"
        CAcert.get_subject().O = "SiriServer by Eichhoernchen"
        CAcert.get_subject().OU = "SiriServer Certificate Authority"
        CAcert.get_subject().CN = "SiriServer Fake CA Certificate"
        CAcert.set_serial_number(1000)
        CAcert.gmtime_adj_notBefore(0)
        CAcert.gmtime_adj_notAfter(10*365*24*60*60)
        CAcert.set_issuer(CAcert.get_subject())
        CAcert.set_pubkey(ca_key)
        
        extensions = []
        crypto.X509ExtensionType
        extensions.append(crypto.X509Extension("basicConstraints", critical=False, value="CA:TRUE"))
        extensions.append(crypto.X509Extension("subjectKeyIdentifier", critical=False, value="hash", subject=CAcert))
        CAcert.add_extensions(extensions)
        # we need to set this separatly... don't know why...
        CAcert.add_extensions([crypto.X509Extension("authorityKeyIdentifier", critical=False, value="keyid:always", issuer=CAcert)])
        CAcert.sign(ca_key, 'sha1')
        fhandle = open(ROOT_CA_CERT_FILE, "wb")
        fhandle.write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, CAcert)
            )
        fhandle.close()
        fhandle = open(ROOT_CA_KEY_FILE, "wb")
        fhandle.write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, ca_key)
            )
        fhandle.close()
        
        print "I successfully created a CA for you, will now use it to create SSL certificates."
        # create a key pair
        k2 = crypto.PKey()
        k2.generate_key(crypto.TYPE_RSA, 2048)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "DE"
        cert.get_subject().ST = "NRW"
        cert.get_subject().L = "Aachen"
        cert.get_subject().O = "SiriServer by Eichhoernchen"
        cert.get_subject().OU = "SiriServer Certificate Authority"
        
        hostname = gethostname()
        print "We need to set the correct address of this machine in the certificate."
        print "I will now query your system for its name. But it might be that you want to use a DNS name I cannot find.\n"
        print "-------- IMPORTANT ----------"
        print "Your system tells me that your hostname/IP is: {0}".format(hostname)
        sys.stdout.write("Do you want to use this information (y/n): ")
        answer = sys.stdin.readline().lower()
        if "no" in answer or "n" in answer:
            sys.stdout.write("Okay what do you want the hostname to be: ")
            hostname = sys.stdin.readline().strip()
            print "Okay thanks I will now be using {0}".format(hostname)
            
        cert.get_subject().CN = hostname
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(CAcert.get_subject())
        cert.set_pubkey(k2)
        
        extensions = []
        crypto.X509ExtensionType
        extensions.append(crypto.X509Extension("basicConstraints", critical=False, value="CA:FALSE"))
        extensions.append(crypto.X509Extension("subjectKeyIdentifier", critical=False, value="hash", subject=cert))
        extensions.append(crypto.X509Extension("authorityKeyIdentifier", critical=False, value="keyid:always", subject=CAcert, issuer=CAcert))
        cert.add_extensions(extensions)
        
        cert.sign(ca_key, 'sha1')
        fhandle = open(SERVER_CERT_FILE, "wb")
        fhandle.write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
            )
        fhandle.close()
        fhandle = open(SERVER_KEY_FILE, "wb")
        fhandle.write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k2)
            )
        fhandle.close()
        
        print """
        \t\t\t ------------ IMPORTANT ------------\n\n
        \t\tAll certificates have been generated... You must now install the CA certificate on your device\n\n
        \t\tThe file is located at keys/ca.pem in your SiriServer root\n\n
        \t\tMake sure to uninstall an old CA certificate first"\n\n
        \t\tTHE CERTIFICATES MUST MATCH! IF YOU DID THIS HERE BEFORE, THE OLD ca.pem WON'T WORK ANYMORE\n
        \t\tYou can just EMail the keys/ca.pem file to yourself\n
        """
    
        
def main():
    
    parser = OptionParser()
    parser.add_option('-l', '--loglevel', default='info', dest='logLevel', help='This sets the logging level you have these options: debug, info, warning, error, critical \t\tThe standard value is info')
    parser.add_option('-p', '--port', default=4443, type='int', dest='port', help='This options lets you use a custom port instead of 443 (use a port > 1024 to run as non root user)')
    parser.add_option('--logfile', default=None, dest='logfile', help='Log to a file instead of stdout.')
    parser.add_option('-m', '--maxConnections', default=None, type='int', dest='maxConnections', help='You can limit the number of maximum simultaneous connections with that switch')
    (options, _) = parser.parse_args()
    
    x = logging.getLogger()
    x.setLevel(log_levels[options.logLevel])
    
    if options.logfile != None:
        h = logging.FileHandler(options.logfile)
    else:
        h = logging.StreamHandler()
    
    f = logging.Formatter(u"%(levelname)s %(message)s")
    h.setFormatter(f)
    x.addHandler(h)
    
    create_self_signed_cert()
    
    try: 
        from twisted.internet import epollreactor
        epollreactor.install()
    except ImportError:
        x.debug("System does not support epoll")
        x.debug("-> Will use simple poll")
        try:
            from twisted.internet import pollreactor
            pollreactor.install()
        except ImportError:
            x.debug("System does not support poll")
            x.debug("-> Will use default select interface")
    from twisted.internet import reactor

    
    x.info("Starting server on port {0}".format(options.port))
    reactor.listenSSL(options.port, SiriFactory(options.maxConnections), ssl.DefaultOpenSSLContextFactory(SERVER_KEY_FILE, SERVER_CERT_FILE))
    reactor.run()
    x.info("Server shutdown complete")
    
if __name__ == "__main__":
    main()
