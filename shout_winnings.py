#!/usr/bin/env python3
import twitter
from os import environ
import psycopg2
import sys
from random import randint

api = twitter.Api(consumer_key=environ.get('TWIT_CON_KEY'),
                  consumer_secret=environ.get('TWIT_CON_SEC'),
                  access_token_key=environ.get('TWIT_ACC_KEY'),
                  access_token_secret=environ.get('TWIT_ACC_SEC'))

try:
    conn = psycopg2.connect("dbname='dnd_database' user='postgres' host='localhost' password='4339cc5bcd3dde693e9e96925014f71b' port='2619'")
except Exception as e:
    error_log = open("unheard_shouts/error_log", 'a')
    error_log.write("ERROR: " + str(e) + "\n")
    error_log.close()
    sys.exit()

cur = conn.cursor()
cur.execute("SELECT reltuples AS approximate_row_count FROM pg_class WHERE relname = 'scraped_data'")
count = cur.fetchall()

exclamation = ["Huzzah", "Hurrah", "Wooooo", "Avast", "Tally-ho", "Rah rah", "Yippee", "BOOM", "Va-va-voom", "Holy moly", "ROFL"]
taken = ["pilfered", "filched", "purloined", "misappropriated", "burglarized", "pillaged", "pinched", "swindled", "liberated", "defrauded", "lifted"]

status = api.PostUpdate(exclamation[randint(0,10)] + '! We\'ve ' + taken[randint(0,10)] + ' metadata from ' + str(int(count[0][0])) + ' websites so far!')
