# skrurai-bot
> I’m a Twitter bot! 🤖

# Features/Scripts/Modes
Currently, *skrurai-bot* is running the **math-evaluation script** which will evaluate math equations if the bot is mentioned on Twitter in THIS format:
`@0skrurai evaluate:<math-equation>`

Otherwise, all previous 'scripts' or 'modes' that skrurai-bot once ran are all located in `presets.py` with brief description of what they are.

# Clear/Clean all tweets and likes
Cleaning the bot's tweets and likes is as simple as 1,2,3.
-   ### Import clean
    ```python
    from clean import clean
    ```

-   ### Run the function
    ```python
    clean(api_object, clean_statuses, clean_likes)
    ```

    -   api_object
        -   the variable with `tweepy.API(auth)`
    -   clean_statuses
        -   boolean - If true, Cleans all the statuses except statueses with (🚫) in it.
    -   clean_likes
        -   boolean - If true, Clean all the statuses that the bot have liked before.

-   ### View the bot's profile
    -   As of now, the script requires manual termination. So when the bot is 'cleaned', Terminate the script in terminal by pressing `Ctrl + C` or `Ctrl + Z`

# Contribution Guide (Or first time usage)
-   ### Install  all the required packages first
    ```shell
    pip install -r requirements.txt 
    ```

-   ### Include credentials by Twitter in `/credentials.py`
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
