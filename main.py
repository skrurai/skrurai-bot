# Import tweepy
import tweepy
from credentials import *
from time import sleep

from templates import footer

# Here is where we initialise tweepy
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# All the id of replied tweets
replied = []

while True:
    for m in api.mentions_timeline():

        # Pick out the JSON
        mention = m._json

        # Get the ID and TEXT CONTENTS of the mentioned tweet
        id = mention['id']
        text = mention['text']

        # If the ID is not in replied (because everytime it is replied to, the ID is pushed to replied)
        if(id not in replied):

            # Push to replied array
            replied.append(id)

            # Try block so that robot won't just quit
            try:
                evaluate_text = text.split(':')[1].strip().lstrip('0')

                # create the status
                status = f'The answer is {eval(evaluate_text)} {footer}'

                # print it
                print(status)

                # reply to it
                api.update_status(status=status, in_reply_to_status_id=id)

                print('Replied')

            # If any error come by, execute the code in the block
            except:
                print('Something Went Wrong')

    sleep(10)