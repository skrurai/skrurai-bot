
def push_id(id):
    try:
        import json
    except:
        print('Error importing json')
    
    with open('replied_to_tweets.json') as json_file:  
        data = json.load(json_file)
        data.append(id)

        with open('replied_to_tweets.json', 'w') as outfile:
            json.dump(data, outfile)

def ids():

    try:
        import json
    except:
        print('Error importing json')
    
    with open('replied_to_tweets.json') as json_file:  
        data = json.load(json_file)
        return data

def clear_all():
    try:
        import json
    except:
        print('Error importing json')
    
    with open('replied_to_tweets.json', 'w') as outfile:
        json.dump([], outfile)
