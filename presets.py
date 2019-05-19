# Giveaway Bot

# Usually giveaway posts will require the user to follow, retweet and like, So this bot searches for tweets that have 'giveaway' in it and retweets, follows or likes the tweet according to the argument given.

def giveaway_bot(api_object, follow_user, retweet_tweet, like_tweet):
    search = api_object.search(q='giveaway', rpp=100)

    for item in search:
        json = item._json
        id = json['id']

        author_username = json['user']['screen_name']

        # If the tweet is not a reply, in_reply_to_status_id won't exist
        if(not json['in_reply_to_status_id']):

            if(follow_user):
                # Folow the user
                api_object.create_friendship(author_username)

            if(retweet_tweet):
                # Retweet tweet
                api_object.retweet(id)

            if(like_tweet):
                # Like the tweet
                api_object.create_favorite(id)