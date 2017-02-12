#!/usr/bin/env python3
import twitter
from os import environ

api = twitter.Api(consumer_key=environ.get('TWIT_CON_KEY'),
                  consumer_secret=environ.get('TWIT_CON_SEC'),
                  access_token_key=environ.get('TWIT_ACC_KEY'),
                  access_token_secret=environ.get('TWIT_ACC_SEC'))
status = api.PostUpdate('Huzzah! This is a test.')
print(status.text)
