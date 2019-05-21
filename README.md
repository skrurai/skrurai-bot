# v2.0
-   Added a new way of how to make a command (read at `commands.py`). (Please note that previous versions of commands will break!)
-   More optimization (not so sure about this...)
# @next branch
The @next branch is the development branch for the upcoming version/iteration of skrurai-bot. The features are very very experimental and developers needs to be cautious

# Table of Contents
| Content               | Description           |
|:-------------         |:-------------|
| [User Agreeement](#user-agreement)       |An agreement that is binded automatically when a twitter user uses any of the bot's feature(s) |
| [Definitions](#Definitions)              | Words used in the documentations with its meaning      |
| [Commands](#commands)         | How to use commands      |
| [Flow of program](#Flow-of-program) | How the program works and the 'flow' it goes through to find @mentioned tweets |
| [Contribution](#Contribution) | Contribution Guide on how to contribute features/commands|

# User Agreement
-   By using any of skrurai-bot's features, the user is automatically binded to an agreement that basically tells how any form of data is handled.
    -   Data collected:
        -   Twitter Status ID
            -   The ID is collected to prevent duplicate replies to a tweet. While we take certain measures to ensure the data is not publicly available, We can't ensure that the ID will not be leaked. The ID basically leads to the status containing the command you send to the bot.

# Definitions
-   Some words that is used throughout this documentation and its meanings
    -   Status(es) / Tweet(s)
        -   A twitter post
    -   Mention(s)
        -   A new status containing: @ and followed by the username of the twitter bot
    -   Bot(s)
        -   The twitter bot
    -   Username(s)
        -   Screen name for twitter (@username)

# Commands
To use the twitter bot, One must @mention the bot in the format: [command:text]. To contribute a command, see [Contribution](#contribution)

Examples:
```
Tweet: @skruraibot [math:1+2]
Reply: The answer is: 3

Tweet: [math: 1+2]
Reply: None, robot is not mentioned in the status

Tweet: @skruraibot [semicaps:hello]
Reply: HeLlO

Tweet: @skruraibot [commands:]
Reply: <Robot will then reply with all the available commands>

```

# Flow of program:
-   See all tweets that mentioned the bot
-   See if there is a command in the tweet
-   Check if the tweet is replied to already or not (by checking against a json file of all the tweets' id replied to)

#  Contribution
-   Install all the required pacakges
-   Create a file called `credentials.py` in the root folder, it should be in the format below with the same variable names.
    ```python
    consumer_token = 'CONSUMER_TOKEN_HERE'
    consumer_secret = 'CONSUMER_SECRET_HERE'
    key = 'ACCESS_KEY_HERE'
    secret = 'ACCESS_SECRET_HERE'
    ```
-   Create a file called `replied_to_tweets.json` in the root folder, this file will be used to check the 3rd step in the [Flow of program](#flow-of-program). It should only contain exactly this:
    ```json
    []
    ```

-   Done, now you can code away!
    -   To contribute a command, proceed to `/commands.py`.
    -   To contibute to how to bot works, proceed to `/main.py`.