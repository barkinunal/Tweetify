import requests
import spotify_token as st
import sys
from time import sleep
from collections import defaultdict
import tweepy

counter = 0
previous_response = -1
song_name = ""
artist_name = ""

auth = tweepy.OAuthHandler(sys.argv[3], sys.argv[4])
auth.set_access_token(sys.argv[5], sys.argv[6])

api = tweepy.API(auth)

songs = defaultdict(int)

while counter < 100 :

    data = st.start_session(sys.argv[1], sys.argv[2])

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + data[0],
    }

    params = (
        ('market', 'ES'),
    )

    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers, params=params)

    if response.status_code == 200 :
        x = response.json()

        if (song_name == x["item"]["name"] and artist_name == x["item"]["artists"][0]["name"]) :
            continue

        song_name = x["item"]["name"]
        artist_name = x["item"]["artists"][0]["name"]
        string = artist_name + " - " + song_name
        
        if songs[string] < 2 :
            print(string)
            api.update_status('Barkın is currently listening "' + string + '"' )
            songs[string] += 1

    elif response.status_code == 204 and previous_response != 204:
        print("Not playing at the moment")
    elif response.status_code == 401 :
        print("Auth Error")

    counter += 1
    previous_response = response.status_code
    sleep(60)

