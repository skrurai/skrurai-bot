
# This file is a handler to open the json file containing all the IDs of the tweets replied to, there is some default function(s) to assist in the handling of the file.
import json

# Push an ID
def push_id(id):
    with open('replied_to_tweets.json') as json_file:  
        data = json.load(json_file)
        data.append(id)

        with open('replied_to_tweets.json', 'w') as outfile:
            json.dump(data, outfile)

# Returns all the IDs
def ids():
    with open('replied_to_tweets.json') as json_file:  
        data = json.load(json_file)
        return data

# Clear all the IDs
def clear_all():
    with open('replied_to_tweets.json', 'w') as outfile:
        json.dump([], outfile)
