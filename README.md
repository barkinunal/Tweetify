
# Tweetify - Tweet Your Currently Playing Songs on Spotify.

This script gets your currently listening song and tweets it to your account.

In order to use this bot, you must have  **Spotify developer account**  and  **Twitter developer account**. You will use your accounts' **Client IDs** and **Client Secrets**.

### First of all, create a virtual environment with

       python3 -m venv spotify-bot

### Then, you need to install the libraries below with "pip/pip3 install" :

-   requests
-   tweepy
-   spotify-token

### Create a file called _"config.txt"_ and put these informations one by one at each a lines.

	SPOTIFY_USERNAME 
	SPOTIFY_PASSWORD 
	TWITTER_CONSUMER_API_KEY
	TWITTER_CONSUMER_API_SECRET
	TWITTER_ACCESS_TOKEN
	TWITTER_ACCESS_TOKEN_SECRET
	YOUR_NAME

### Finally, you can run the script as follows :
 

	python3 bot.py

#### While running the script, bot will create a file named _"db.txt"_. It keeps what you played before. Do not delete it.
