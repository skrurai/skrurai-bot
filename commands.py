import re
footer = '\n\n\U0001F916'

# Evaluate math equations
def math(api_object, tweet_id, screen_name, input):

    # check if there is NO letters
    if re.search(r'[a-zA-Z]', input) is None:
        try:
            eval(input.lstrip('0'))
        except:
            try:
                api_object.update_status(status=f'@{screen_name} The command does not accept complex math equations {footer}', in_reply_to_status_id=tweet_id)
                print(f'JUST_REPLIED: {tweet_id}')
            except:
                print(f'DUPLICATE_STATUS: {tweet_id}')
        else:
            try:
                api_object.update_status(status=f'@{screen_name} The answer is: {eval(input.lstrip(0))} {footer}', in_reply_to_status_id=tweet_id)
                print(f'JUST_REPLIED: {tweet_id}')
            except:
                print(f'DUPLICATE_STATUS: {tweet_id}')
    else:
        try:
            api_object.update_status(status=f'@{screen_name} The command does not letters as part of the equation {footer}', in_reply_to_status_id=tweet_id)
            print(f'JUST_REPLIED: {tweet_id}')
        except:
            print(f'DUPLICATE_STATUS: {tweet_id}')
        

def mock(api_object, tweet_id, screen_name, input):
    mock_text = []

    for index, letter in enumerate(input.lower()):
        if index % 2 is 0:
            mock_text.append(letter.upper())
        else:
            mock_text.append(letter)

    return_string = ''.join(mock_text)
    # TODO: tweet with picture

    try:
        api_object.update_with_media(filename='./assets/mock.jpg', status=f'@{screen_name} {return_string} {footer}', in_reply_to_status_id=tweet_id)
        print(f'JUST_REPLIED: {tweet_id}')
    except:
        print(f'DUPLICATE_STATUS: {tweet_id}')
    # TODO: log that duplicate

def joke(api_object, tweet_id, screen_name, input):
    import requests
    json = requests.get('https://official-joke-api.appspot.com/random_joke').json()

    joke = json['setup'] + ' ' + json['punchline']
    
    try:
        api_object.update_status(status=f'@{screen_name} {joke} {footer}', in_reply_to_status_id=tweet_id)
        print(f'JUST_REPLIED: {tweet_id}')
    except:
        print(f'DUPLICATE_STATUS: {tweet_id}')