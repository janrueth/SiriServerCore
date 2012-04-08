from twisted.internet import threads, defer
import contextlib
import logging
import urllib2

class AsyncOpenHttp(object):
    def __init__(self, callback):
        super(AsyncOpenHttp, self).__init__()
        self.callback = callback
    
    def make_google_request(self, flac, requestId, dictation, language="de-DE", allowCurses=True):
        d = threads.deferToThread(self.run, flac, requestId, dictation, language, allowCurses)
        d.addCallback(self.callback, requestId, dictation)
        d.addErrback(self.onError)
        return d
    
    def onError(self, failure):
        failure.trap(defer.CancelledError)
        logging.getLogger().info("Google request canceled")
        pass
    
    def getWebsite(self, url, timeout=5):
        '''
            This method retrieved the website at the url encoded url
            if this method fails to retrieve the website with the given timeout
            or anything else, None is returned
        '''
        try:
            with contextlib.closing(urllib2.urlopen(url, timeout=timeout)) as page:
                body = page.read()
                return body
        except:
            pass
        return None
    
    def run(self, flac, requestId, dictation, language, allowCurses):
        url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter={0}&lang={1}&maxresults=6".format(0 if allowCurses else 2, language)
        req = urllib2.Request(url, data = flac, headers = {'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent': 'Siri-Server'})
        return self.getWebsite(req, timeout=10)
