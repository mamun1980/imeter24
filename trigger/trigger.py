#!/usr/local/bin/python
# encoding: utf-8
"""
online data importer for premier elevator
"""

import sys, os, socket
import getopt
import time
import datetime
from datetime import date
import select
from urllib import unquote_plus
import logging

import select
import psycopg2
import psycopg2.extensions

from os import listdir
from os.path import isfile, join

from elasticsearch import Elasticsearch
es = Elasticsearch()



timesleep = time.sleep
date = str(date.today())
senddate = date[2] + date[3] + date[5] + date[6] + date[8] + date[9] 
senddate2 = date[0] + date[1] + date[2] + date[3] + date[5] + date[6] + date[8] + date[9] 

uu = time.localtime()

#Open The Databases (test and live)
print "Opening the test database"
conntestdb = psycopg2.connect(host='localhost', port=5432, database='premier_test', user='scom_test', password='Testxxyy')
conntestdb.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
testdb = conntestdb.cursor()

#testdb.execute('''create table users (username text primary key, whatever int4);''')

testdb.execute('''create function new_user_notify() returns trigger as $$
begin
    perform pg_notify('new_user', NEW.contact_name);
    return NEW;
END;
$$ language plpgsql;''')


testdb.execute('''create trigger new_user_notify after UPDATE on contacts_contact for each row execute procedure new_user_notify();''')





#create the event listener

testdb.execute("LISTEN new_user;")


print "Waiting for notifications on channel 'new_user'"
while 1:
    if select.select([conntestdb],[],[],5) == ([],[],[]):
        print "Timeout"
    else:
        conntestdb.poll()
        while conntestdb.notifies:
            notify = conntestdb.notifies.pop()
            print "Got NOTIFY:", notify.pid, notify.channel, notify.payload
			

sys.exit()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime(2010, 10, 10, 10, 10, 10)
}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
	


