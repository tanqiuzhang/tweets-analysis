#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:49:58 2018

@author: ray
"""


import tweepy
import json
import jsonpickle


ACCESS_TOKEN = '1633390099-Ny0Okjv4hstXxXUoDBMbztId8Nk1F1vx8nFVssA'
ACCESS_SECRET = 'gv4e2qPaq9N3WRbaqDRIHiuGd3yNEDaUS0Ml2bZ9yUIDq'
CONSUMER_KEY = 'qYjxNQqw2CbOADiLvcMAYqQlK'
CONSUMER_SECRET = 'g9wwGCrVZm1E8LAMvPwajqZjhCue8cyYmFP3UyAzvPFEBrfjAl'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
max_tweets = 10000

'''
tweets = []
for tweet in tweepy.Cursor(api.search, q='#Bitcoin', rpp=100).items(max_tweets):
    tweets.append(tweet._json['text'])
    pass
'''

tweet_count = 0
with open('tweets.json', 'w') as f:
    for tweet in tweepy.Cursor(api.search, q='#Bitcoin').items(max_tweets):
        if tweet.place is not None:
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweet_count += 1
    print('Downloaded {0} tweets.'.format(tweet_count))
                            