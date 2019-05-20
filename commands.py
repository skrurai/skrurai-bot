# HERE LIES ALL THE COMMANDS
# TO ADD NEW COMMANDS, NAME A FUNCTION THAT TAKES THE 'text' PARAMETER
# IT MUST RETURN A VALUE

# So if the tweet has [math:92+1]
# The bot will run math('92+1')
# and the math function will evaluate the result and return
# Same with your commands.

# Evaluate math equations
def math(text):
    final = text.lstrip('0')
    
    # If can evaluate, it is a math equation
    try:
        eval(final)
        return f'The answer is: {eval(final)}'
    except:
        return 'Not a VALID math equation!'

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
def yesorno_experimental(text):
    try:
        import random
    except:
        import random

    choice = random.choice([True, False])

    if(choice == True):
        return 'Yes!'
    if(choice == False):
        return 'No!'

# Returns all the possible commands/functions
def commands(text):
    commands = [func for func in globals() if not func.startswith('__')]
    return 'All the commands \U0001F4BB are:\n\n' + "\n".join(commands)