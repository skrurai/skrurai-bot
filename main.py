# Import packages
import tweepy
from credentials import *
from id_handler import push_id, ids
from time import sleep
from commands import *
import re

# Tweepy initialisation
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# -   See all tweets that mentioned the bot
# -   See if there is a command in the tweet
# -   Check if the tweet is replied to already or not (by checking against a json file of all the tweets' id replied to)

# Main Function (invoking below)
def main():
    while True:
        # Loop in the timeline
        for m in api.mentions_timeline():
            mention = m._json

            id = mention['id']
            status = mention['text']
            screen_name = mention['user']['screen_name']

            inner_brackets = status[status.find('[')+1:status.find(']')]
            command = inner_brackets.split(':')[0]
            input = inner_brackets.split(':')[1]

            # If not replied to
            if(id not in ids()):
                # run the function
                try:
                    globals()[command](api, id, screen_name, input)
                    push_id(id)
                except:
                    # Log that it is not a real function
                    print(f'NOT_A_FUNCTION: {id}')
            elif id in ids():
                # log that is previously replied
                print(f'PREVIOUSLY_REPLIED: {id}')
        sleep(30)

if __name__ == "__main__":
    main()