from ctypes import *
import ctypes.util
import math
import os
import struct
import tempfile

libflac_name = ctypes.util.find_library('FLAC')
if libflac_name == None:
    print "Could not find libFLAC"
    exit()
libflac = CDLL(libflac_name)


def writeCallBack(encoder, buf, numBytes, samples, current_frame, client_data):
    print "Test"
    instance = cast(client_data, py_object).value
    return Encoder.internalCallBack(instance, encoder, buf, numBytes, samples, current_frame)



class Encoder:
    
    def __init__(self):
        self.encoder = None
        self.output = None
        self.filename = None

    
    def initialize(self, sample_rate, channels, bps):
        libflac.FLAC__stream_encoder_new.restype = c_void_p
        libflac.FLAC__stream_encoder_set_verify.argtypes = [c_void_p, c_bool]
        libflac.FLAC__stream_encoder_set_verify.restype = c_bool
        
        libflac.FLAC__stream_encoder_set_compression_level.argtypes = [c_void_p, c_uint]
        libflac.FLAC__stream_encoder_set_compression_level.restype = c_bool
        
        libflac.FLAC__stream_encoder_set_channels.argtypes = [c_void_p, c_uint]
        libflac.FLAC__stream_encoder_set_channels.restype = c_bool
        
        libflac.FLAC__stream_encoder_set_bits_per_sample.argtypes = [c_void_p, c_uint]
        libflac.FLAC__stream_encoder_set_bits_per_sample.restype = c_bool
        
        libflac.FLAC__stream_encoder_set_sample_rate.argtypes = [c_void_p, c_uint]
        libflac.FLAC__stream_encoder_set_sample_rate.restype = c_bool
        
        libflac.FLAC__stream_encoder_set_total_samples_estimate.argtypes = [c_void_p, c_uint64]
        
        libflac.FLAC__stream_encoder_set_total_samples_estimate.restype = c_bool
        
        writeCallBackFUN = CFUNCTYPE(c_uint, c_void_p, c_char_p, c_size_t, c_uint, c_uint, c_void_p)
        
        libflac.FLAC__stream_encoder_init_stream.argtypes = [c_void_p, writeCallBackFUN, c_void_p, c_void_p, c_void_p, py_object]
        
        libflac.FLAC__stream_encoder_process.restype = c_bool
        libflac.FLAC__stream_encoder_process.argtypes = [c_void_p, POINTER(POINTER(c_int32)), c_uint]
        
        libflac.FLAC__stream_encoder_process_interleaved.restype = c_bool

        libflac.FLAC__stream_encoder_process_interleaved.argtypes = [c_void_p, c_void_p, c_uint]
        
        libflac.FLAC__stream_encoder_finish.argtypes = [c_void_p]
        libflac.FLAC__stream_encoder_finish.restype = c_bool
        libflac.FLAC__stream_encoder_delete.argtypes = [c_void_p]
        
        libflac.FLAC__stream_encoder_init_file.argtypes = [c_void_p, c_char_p, c_void_p, c_void_p]
        
        self.encoder = libflac.FLAC__stream_encoder_new()
        
        ok = 1

        ok &= libflac.FLAC__stream_encoder_set_verify(self.encoder, True)

        ok &= libflac.FLAC__stream_encoder_set_compression_level(self.encoder, 5)
        ok &= libflac.FLAC__stream_encoder_set_channels(self.encoder, channels)
        ok &= libflac.FLAC__stream_encoder_set_bits_per_sample(self.encoder, bps);
        ok &= libflac.FLAC__stream_encoder_set_sample_rate(self.encoder, sample_rate);
        
        
        self.output = ""
        #libflac.FLAC__stream_encoder_init_stream(self.encoder, writeCallBackFUN(writeCallBack), None, None, None, py_object(self))
        tmpFile = tempfile.NamedTemporaryFile(delete=False)
        tmpFile.close()
        self.filename = tmpFile.name
        libflac.FLAC__stream_encoder_init_file(self.encoder, self.filename, None, None)
        if not ok:
            print "Error initializing libflac"
            exit()
    
    def internalCallBack(self, encoder, buf, numBytes, samples, current_frame):
        self.output += string_at(buf, numBytes)
        print self.output
        return 0
    


    def encode(self, data):
        length = int(len(data)/2)
        int16s = struct.unpack('<' + ('h'*length), data)
        int32s = struct.pack('@' + ('i'*length), *int16s)
        libflac.FLAC__stream_encoder_process_interleaved(self.encoder, int32s, length)

    def getBinary(self):
        f = open(self.filename, 'r')
        flac = f.read()
        f.close()
        return flac
        
    def finish(self):
        if self.encoder:
            libflac.FLAC__stream_encoder_finish(self.encoder)
    
    def destroy(self):
        if self.encoder:
            libflac.FLAC__stream_encoder_delete(self.encoder)
            os.unlink(self.filename)
            self.encoder = None
