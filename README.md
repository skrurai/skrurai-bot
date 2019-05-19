# skrurai-bot
I’m a Twitter bot! 🤖, Expected to be Fully functional by 15 July 2019!

## Mode
Currently, the bot is under beta-testing and there is no specific mode. Thorough testing is ongoing to prepare for 15 July 2019

## Definitions
Some words that is used throughout this documentation and its meanings
-   Mode(s)
    -   The current feature or script that the bot is running.
-   Status(es)
    -   A twitter post
-   Bot(s)
    -   The twitter bot


## Clear/Clean all tweets and likes
Cleaning the bot's tweets and likes is simple.
-   Run the file from the terminal
    ```shell
    python3 clean.py
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
