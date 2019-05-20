# HERE LIES ALL THE COMMANDS
# TO ADD NEW COMMANDS, NAME A FUNCTION THAT TAKES THE 'text' PARAMETER
# IT MUST RETURN A VALUE

# So if the tweet has [math:92+1]
# The bot will run math('92+1')
# and the math function will evaluate the result and return
# Same with your commands.

# Evaluate math equations
def math(text):

    try:
        # Import regex
        import re

        # Strip any numbers
        final = text.lstrip('0')

        # See if letters exist, if it exists, it will return a value other than None
        if(re.search('[a-zA-Z]+', final) is not None):

            # Raise an exception
            raise Exception('Letter')
        else:

            # If its a number
            try:
                # Evaluate
                return f'The answer is: {eval(final)}'
            except:
                return 'Can\'t handle complex math equations!!'
            
    except:
        return '[math:] does not accept any letters'
    
    


# Returns semi caps
def semicaps(text):
    return_string = []

    for index,letter in enumerate(text):
        if(index % 2 == 0):
            return_string.append(letter.upper())
        else:
            return_string.append(letter.lower())
    
    return ''.join(return_string)

# Returns yes or no randomly
def yesorno(text):
    try:
        import random
    except:
        import random

    choice = random.choice([True, False])

    if(choice == True):
        return 'Yes!'
    if(choice == False):
        return 'No!'

# Sends a url of a cat picture:
def cat(text):
    try:
        import requests
    except:
        return 'Something Went Wrong!'

    try:
        url = requests.get('https://api.thecatapi.com/v1/images/search?size=full').json()[0]['url']
        return f'Here is a picture of a cat: {url}'
    except:
        return 'Something Went Wrong while getting the picture!!!'

# Returns all the possible commands/functions
def commands(text):
    commands = [func for func in globals() if not func.startswith('__')]
    return 'All the commands \U0001F4BB are:\n\n' + "\n".join(commands)