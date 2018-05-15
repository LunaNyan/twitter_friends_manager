#!/usr/bin/python3

try:
    import configparser
except ImportError as _:
    import ConfigParser as configparser

import datetime
import tweepy

Config = configparser.ConfigParser()
Config
Config.read("access_key.txt")

aKey = Config['access_key']['access_token_key']
aSecret = Config['access_key']['access_token_secret']

consumerKey = 'SqDP4fVta35RqLfHENK7lGCs7'
consumerSecret = 'UNDofhfpfIkgRMyGfsE0jMowWf3yasdi71TNxABSqDEnJ0u1Aj'

#auth.OAuthHandler 객체 반환
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)

accessToken = aKey
accessTokenSecret = aSecret 

#auth.OAuthHandler r객체에 엑세스토큰 지정
auth.set_access_token(accessToken, accessTokenSecret)

#API 클래스의 인스턴스 반환 - 읽기, 트윗, 리트윗, DM
api = tweepy.API(auth)

#트윗포스트
tweet = str(datetime.datetime.now()) + " 테스트 포스트하기 "
api.update_status(status=tweet)

print("Success")
print()

#읽기
tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.text)
