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

from id_handler import push_id, ids

# Import necessary libraries
from time import sleep
from commands import *

# Tweepy initialisation
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# FLOW OF PROGRAM
# (1) SEE ALL MENTIONS
# (2) CHECK IF THE TEXT IS A COMMAND OR NOT
# (3) CHECK IF REPLIED TO ALREADY OR NOT
# (4) REPLIED

# Main Function (invoking below)
def main():
    # Run in a loop
    while True:
        print('\nLOOP')
        print(moment.date(moment.now()).strftime("%d/%m/%Y %H:%M:%S"))

        # (1)
        for m in api.mentions_timeline():
            mention = m._json

            status_text = mention['text'].lower()
            screen_name = f"@{mention['user']['screen_name']}"
            id = mention['id']

            text_in_brackets = status_text[status_text.find('[') + 1 : status_text.find(']')]

            command = text_in_brackets.split(':')[0]
            text = text_in_brackets.split(':')[1]

            # (2)
            try:
                returnstring = globals()[command](text)
            except:
                print(f'Not A Command {id}')
            else:
                # (3)
                if id not in ids():
                    # push the id
                    push_id(id)

                    try:
                        # (4)
                        api.update_status(status=f'{screen_name} {returnstring}', in_reply_to_status_id=id)
                        print(f'Just Replied {id}')
                    except:
                        print(f'Duplicate Status {id}')
                else:
                    # print replied
                    print(f'Previously Replied {id}')

        # Sleep for 30 secs and then loop again
        sleep(30)

if __name__ == "__main__":
    main()