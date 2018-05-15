#!/usr/bin/python3

try:
    import configparser
except ImportError as _:
    import ConfigParser as configparser

import datetime
import tweepy

Config = configparser.ConfigParser()
Config
Config.read("settings.txt")

cKey = Config['auth']['consumer_key']
cSecret = Config['auth']['consumer_secret']
aKey = Config['auth']['token_key']
aSecret = Config['auth']['token_secret']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)

consumerKey = cKey
consumerSecret = cSecret
accessToken = aKey
accessTokenSecret = aSecret

auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#tweet post test
tweet = str(datetime.datetime.now()) + " test post :)"
api.update_status(status=tweet)

print("Success")
print()

#read timeline
tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.text)
