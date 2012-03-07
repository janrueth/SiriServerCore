#!/usr/bin/python
# -*- coding: utf-8 -*-

from uuid import uuid4
import cPickle
import logging
import sqlite3

__database__ = "database.sqlite3"

def setup():
    conn = getConnection()
    c = conn.cursor()
    c.execute("""
        create table if not exists assistants(assistantId text primary key, assistant assi)
        """)
    conn.commit()
    c.close()
    conn.close()

def getConnection():
    try:
        return sqlite3.connect(__database__, detect_types=sqlite3.PARSE_DECLTYPES, timeout=10.0)
    except sqlite3.Error.OperationalError as e:
        logging.getLogger().error("Connecting to the internal database timed out, there are probably to many connections accessing the database")
        logging.getLogger().error(e)
    return None

class Assistant(object):
    def __init__(self, assistantId=str.upper(str(uuid4()))):
        self.assistantId = assistantId
        self.censorspeech = None
        self.timeZoneId = None
        self.language = None
        self.region = None


def adaptAssistant(assistant):
    return cPickle.dumps(assistant)

def convertAssistant(fromDB):
    return cPickle.loads(fromDB)

sqlite3.register_adapter(Assistant, adaptAssistant)
sqlite3.register_converter("assi", convertAssistant)