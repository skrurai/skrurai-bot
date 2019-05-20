def clean(api_object, clean_statuses, clean_likes, include_string):
    while True:
        if(clean_statuses):
            for status in api_object.user_timeline():
                json = status._json
                id = json['id']
                
                if(include_string not in json['text']):
                    api_object.destroy_status(id)

        if(clean_likes):
            for status in api_object.favorites():
                api_object.destroy_favorite(id=status._json['id'])


# If ran like python3 clean.py instead of importing:
if(__name__ == '__main__'):
    # Import necessary packages
    import tweepy
    from credentials import consumer_secret, consumer_token, key, secret

    # Here is where we initialise tweepy
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)

    # Invoke the clean function
    clean(api, True, True, '\U0001F6AB')