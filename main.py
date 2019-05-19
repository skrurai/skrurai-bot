# Import tweepy
import tweepy

# Libraries

# Includes Credentials with all the consumer token, secret and the access key and secret
from credentials import *

# Library to include a string that includes the time and date of the tweet
import include_date

# Here is where we initialise tweepy
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Main code starts here
timeline = api.user_timeline()

for status in timeline:
    json = status._json

    print(json['id_str'])