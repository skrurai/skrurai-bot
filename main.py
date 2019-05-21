# Import packages
import tweepy
from credentials import *
from id_handler import ids, push_id
from time import sleep
from commands import *
import re

footer = '\n\n\U0001F916'

# Tweepy initialisation
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Main Function (invoking below)
def main():
    # Loop in the timeline
    for m in api.mentions_timeline():
        mention = m._json

        # Get the tweet id, the text and the username
        tweet_id = mention['id']
        status = mention['text']
        screen_name = mention['user']['screen_name']

        # For tweets without [], the status.find will return -1, so as to say, the inner_brackets is finding anything between [] or else the variable will just be NONE
        inner_brackets = status[status.find('[')+1:status.find(']')] if status.find('[') is not -1 else None

        # When split [command:input_text], so split only if inner_brackets is not None else the command and input_text will be an empty string
        command = inner_brackets.split(':')[0] if inner_brackets is not None else ''
        input_text = inner_brackets.split(':')[1] if inner_brackets is not None else ''

        # Check if the ID is part of the ids() (part of the IDs in the JSON file)
        if(tweet_id not in ids()):

            # Run the function

            # Try to see if it will return any error (the ones that return errors are the ones has no function, or function is not available)
            try:

                # What I mean by this is that when the user type in [command:input_text], it WILl execute in python as command(input_text)
                globals()[command](input_text)

                # PUSH THE ID (id_handler library)
                push_id(tweet_id)
            except:

                # (the ones that return errors are the ones has no function, or function is not available)
                # Log that it is not a real function
                print(f'NOT_A_FUNCTION: {tweet_id} {command}')
            else:

                # If no errors, proceed to tweet
                # execution is the return value from the command in commands.py
                execution = globals()[command](input_text)

                # TWEET
                # the return value will check the filename key if there is any filename, if there is, it will update the status with media, else just the text.
                if execution['filename'] is None:
                    tweet_string = execution['return_string']

                    try:
                        api.update_status(status=f'@{screen_name} {tweet_string} {footer}', in_reply_to_status_id=tweet_id)
                        print(f'JUST_REPLIED: {tweet_id} {command}')
                    except:
                        print(f'DUPLICATE_CONTENT_OR_STATUS: {tweet_id} {command}')

                else:
                    filename = execution['filename']
                    tweet_string = execution['return_string']

                    try:
                        api.update_with_media(filename=filename, status=f'@{screen_name} {tweet_string} {footer}', in_reply_to_status_id=tweet_id)
                        print(f'JUST_REPLIED: {tweet_id} {command}')
                    except:
                        print(f'DUPLICATE_CONTENT_OR_STATUS: {tweet_id} {command}')

        elif tweet_id in ids():
            # log that is previously replied
            print(f'PREVIOUSLY_REPLIED: {tweet_id} {command}')


    
if __name__ == "__main__":
    while True:
        main()
        sleep(30)