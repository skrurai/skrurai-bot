# COMMANDS, THE HEART OF THE ROBOT.

# TO MAKE A COMMAND, ONE MUST UNDERSTAND HOW THE COMMANDS WORK
# WHEN A USER MENTION THE BOT WITH [COMMAND:INPUT_TEXT], IT IS THE SAME AS PYTHON EXECUTING COMMAND(INPUT_TEXT)
# SO FOR EXAMPLE: [math:92+1], IT IS THE SAME AS PYTHON EXECUTING math(92+1)

# THE HANDLING OF TWEETING THE COMMAND WILL BE OVER AT MAIN.PY.
# THE COMMAND MUST! MUST!!! RETURN AN OBJECT WITH KEYS 'return_string' and 'filename'
# return_string IS BASICALLY THE RETURN STRING FROM THE COMMAND
# filename IS OPTIONAL, BUT ACCEPTS A FILEPATH TO AN IMAGE OR VIDEO AS A STRING.

# THE COMMAND WILL ACCEPT AN ARGUMENT WHICH IS INPUT - WHICH IS WHATEVER THE INPUT OF THE USER IS (IN STRING)
# Have fun, if you have any more info, please contact me on GitHub or open an issue!

# Evaluate math equations
def math(input):
    import re

    # check if there is NO letters
    if re.search(r'[a-zA-Z]', input) is None:
        try:
            eval(input.lstrip('0'))
        except:
            return_string = 'The command does not accept complex math equations'

            return {
                'return_string': return_string,
                'filename': None
            }
        else:
            evaluated_string = eval(input.lstrip('0'))
            return_string = f'The answer is: {evaluated_string}'

            return {
                'return_string': return_string,
                'filename': None
            }
    else:
        return_string = 'The command does not letters as part of the equation'

        return {
            'return_string': return_string,
            'filename': None
        }
        

def mock(input):
    mock_text = []

    for index, letter in enumerate(input.lower()):
        if index % 2 is 0:
            mock_text.append(letter.upper())
        else:
            mock_text.append(letter)

    return_string = ''.join(mock_text)
    
    return {
        'return_string': return_string,
        'filename': './assets/mock.jpg'
    }

def joke(input):
    import requests
    json = requests.get('https://official-joke-api.appspot.com/random_joke').json()

    joke = json['setup'] + ' ' + json['punchline']
    
    return {
        'return_string': joke,
        'filename': None
    }