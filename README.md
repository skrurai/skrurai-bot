# skrurai-bot@next
The next iteration of skrurai-bot lays here, Ongoing features and development are found here. When stable, it will be merged with the master branch. For the rest of the stuff including user agreement and etc, please visit the master branch.

# v2.0
-   Added a new way of how to make a command (read at `commands.py`). (Please note that previous versions of commands will break!)
-   More optimization (not so sure about this...)

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