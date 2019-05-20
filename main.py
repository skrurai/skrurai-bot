# Import packages
try:
    import tweepy
    import moment
except:
    print('Please install all the required packages')

# Import credentials
try:
    from credentials import *
except:
    print('Please follow the documentation to import credentials')

# Import necessary libraries
from time import sleep
from commands import *

# Tweepy initialisation
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Main Function (invoking below)
def main():
    # Run in a loop
    while True:
        print('LOOP')
        print(moment.date(moment.now()).strftime("%d/%m/%Y %H:%M:%S"))

        # Check all the mentions:
        for m in api.mentions_timeline():

            # Pick out the JSON
            mention = m._json

            # Get the ID and TEXT CONTENTS of the mentioned tweet
            id = mention['id']
            status = mention['text'].lower()
            tweet_author = mention['user']['screen_name']

            # Commands typically look like this [command:text]
            # Program will only evaluate anything inside []
            text_inside_brackets = status[status.find('[') + 1 : status.find(']')]

            # Seperate the command and text
            command = text_inside_brackets.split(':')[0]
            text = text_inside_brackets.split(':')[1]

            # Try seeing if the functions is run-able, if not, it is not a command
            try:
                # It is all global functions including globals
                # Its the same as running command(text) like a function
                return_value = globals()[command](text)

                # Try if can reply or not
                try:
                    api.update_status(status=f'@{tweet_author} {return_value}', in_reply_to_status_id=id)
                    print(f'Just Replied: \n{status}\n')
                
                # Print that its already replied to
                except:
                    print(f'Tweet is replied to already: \n{status}\n')

            # Print that it is not a command
            except:
                print('Not a Command')
                            
            
        # Sleep for 1 minute and then loop again
        sleep(60)

if __name__ == "__main__":
    try:
        main()
    except:
        main()