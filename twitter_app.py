#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:49:58 2018

@author: ray
"""


import tweepy
import json


ACCESS_TOKEN = '1633390099-Ny0Okjv4hstXxXUoDBMbztId8Nk1F1vx8nFVssA'
ACCESS_SECRET = 'gv4e2qPaq9N3WRbaqDRIHiuGd3yNEDaUS0Ml2bZ9yUIDq'
CONSUMER_KEY = 'qYjxNQqw2CbOADiLvcMAYqQlK'
CONSUMER_SECRET = 'g9wwGCrVZm1E8LAMvPwajqZjhCue8cyYmFP3UyAzvPFEBrfjAl'





auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
MAX_TWEETS = 100
tweets = []
for tweet in tweepy.Cursor(api.search, q='#Bitcoin', rpp=100).items(MAX_TWEETS):
    tweets.append(tweet._json['text'])
    pass