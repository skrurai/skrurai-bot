# skrurai-bot
I’m a Twitter bot! 🤖, Expected to be Fully functional by 15 June 2019!

## Commands
To use the twitter bot, One must @mention the bot in the format: [command:text].
For developers, all the commands functions are available at `./commands.py`

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

## Definitions
Some words that is used throughout this documentation and its meanings
-   Mode(s)
    -   The current feature or script that the bot is running.
-   Status(es) / Tweet(s)
    -   A twitter post
-   Bot(s)
    -   The twitter bot
-   Mention(s)
    -   A new status with the twitter bot's username mentioned, usually it contains @ and followed by the username of the twitter bot
-   Username(s)
    -   Screen name for twitter


## Clear/Clean all tweets and likes
Cleaning the bot's tweets and likes is simple.
-   Run the file from the terminal
    ```shell
    python3 _clean_.py
    ```

    -   It is going to clean all the statuses and posts by default (unless the status has the 🚫 emoji somewhere in the status)

-   View the bot's profile
    -   As of now, the script requires manual termination. So when the bot is 'cleaned', Terminate the script in terminal by pressing `Ctrl + C` or `Ctrl + Z`

## Contribution Guide (Or first time usage)
-   ### Install  all the required packages first
    ```shell
    pip install -r requirements.txt 
    ```

-   ### Include credentials by Twitter in `credentials.py`
    ```python

    # Consumer Token
    consumer_token = 'XXX'

    # Consumer Token
    consumer_secret = 'XXX'

    # Access Token
    key = 'XXX'

    # Access Secret
    secret = 'XXX'
    ```

-   ### Code away in `/main.py`
