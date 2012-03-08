try:
    
    try: 
        from twisted.internet import epollreactor
        epollreactor.install()
    except:
        print "Warning Your system does not support epoll"
        
    from twisted.internet import ssl, reactor
    from twisted.internet.protocol import Factory
    
except:
    print "You need to install the twisted python libraries (http://twistedmatrix.com/trac/)\n"
    print "On a debian based system try installing python-twisted\n"
    print "On other systems, you may use easy_install or other package managers\n"
    print "Please refer to the website listed above for further installation instructions\n"
    exit(-1)
from SiriProtocolHandler import SiriProtocolHandler
from optparse import OptionParser
import PluginManager
import db
import logging
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
       

class SiriFactory(Factory):

    def __init__(self):
        self.numberOfConnections = 0
        self.sessionCert = None
        self.sessionCACert = None
        self.dbConnection = None
        
    def buildProtocol(self, addr):
        return SiriProtocolHandler(self, addr)
    
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

def main():

    parser = OptionParser()
    parser.add_option('-l', '--loglevel', default='info', dest='logLevel', help='This sets the logging level you have these options: debug, info, warning, error, critical \t\tThe standard value is info')
    parser.add_option('-p', '--port', default=4443, type='int', dest='port', help='This options lets you use a custom port instead of 443 (use a port > 1024 to run as non root user)')
    parser.add_option('--logfile', default=None, dest='logfile', help='Log to a file instead of stdout.')
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
    
    
    x.info("Starting server on port {0}".format(options.port))
    reactor.listenSSL(options.port, SiriFactory(), ssl.DefaultOpenSSLContextFactory('keys/server.key', 'keys/server.crt'))
    reactor.run()
    x.info("Server shutdown complete")
    
if __name__ == "__main__":
    main()
