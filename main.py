# Import tweepy
import tweepy
from credentials import *
from time import sleep

# Here is where we initialise tweepy
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# while True:
#     print('LOOP')

#     for m in api.mentions_timeline():

#         # Pick out the JSON
#         mention = m._json

#         # Get the ID and TEXT CONTENTS of the mentioned tweet
#         id = mention['id']
#         text = mention['text']

#         print(text)

#     sleep(60)