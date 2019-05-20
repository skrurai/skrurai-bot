# skrurai-bot
skrurai-bot is twitter bot. It is an open-source initiative and it is made to what it is today with the help of other developers and contributors. While proper credit(s) is tried to be given, I, the creator might not be able to reach to all contributors and I would like to extend my sincere apology to you if you are not given proper credit.

# Table of Contents
| Content               | Description           |
|:-------------         |:-------------|
| [User Agreeement](#user-agreeement)       |An agreement that is binded automatically when a twitter user uses any of the bot's feature(s) |
| Definitions              | centered      |
| [Commands](#commands)         | How to use commands      |

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
Tweet: @0skrurai [math:1+2]
Reply: The answer is: 3

Tweet: [math: 1+2]
Reply: None, robot is not mentioned in the status

Tweet: @0skrurai [semicaps:hello]
Reply: HeLlO

Tweet: @0skrurai [commands:]
Reply: <Robot will then reply with all the available commands>

```

# Flow of program:
-   See all tweets that mentioned the bot
-   See if there is a command in the tweet
-   Check if the tweet is replied to already or not (by checking against a json file of all the tweets replied to)

#  Contribution
-   Install all the required pacakges
-   Create a file called `credentials.py`, it should be in the format below with the same variable names.
    ```python
    consumer_token = 'CONSUMER_TOKEN_HERE'
    consumer_secret = 'CONSUMER_SECRET_HERE'
    key = 'ACCESS_KEY_HERE'
    secret = 'ACCESS_SECRET_HERE'
    ```
-   To contribute a command, proceed to `/commands.py`.
-   To contibute to how to bot works, proceed to `/main.py`.