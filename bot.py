"""
Author : Barkın Ünal
Last Update : 31/03/2020
"""

import requests
import sys
from time import sleep
from collections import defaultdict
import tweepy
import spotify_token as st

def init() :
    # Check db and add it into defaultdict songs
    songs = defaultdict(int)

    try :
        db = open("db.txt", "r")
        db_songs = db.readlines()

        for line in db_songs :
            #print("Previous songs in the database : ")
            print(line)
            songs[line[:-1]] += 1

        db.close()

    except IOError:
        print("Database not found. It will be created.")

    return songs

def runner(db, songs) :

    auth = tweepy.OAuthHandler(sys.argv[3], sys.argv[4])
    auth.set_access_token(sys.argv[5], sys.argv[6])

    api = tweepy.API(auth)

    data = st.start_session(sys.argv[1], sys.argv[2])
    token = data[0]
    expiration_date = data[1]

    print("Token : " + token, end="\n\n")
    print("Expiration Date : {}".format(expiration_date), end="\n\n")
    
    counter = 0
    previous_response = -1
    song_name = ""
    artist_name = ""


    while counter < 100 :
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }

        params = (
            ('market', 'ES'),
        )

        response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers, params=params)
        
        if response.status_code == 200 :
            x = response.json()

            # Check if there is still the same song playing
            if (artist_name == x["item"]["artists"][0]["name"] and song_name == x["item"]["name"]) :
                continue

            song_name = x["item"]["name"]
            song_url = x["item"]["external_urls"]["spotify"]
            artist_name = x["item"]["artists"][0]["name"]
            string = artist_name + " - " + song_name

            #print(string)
            
            if songs[string] < 1 :
                try :
                    songs[string] += 1
                    api.update_status(sys.argv[7] + ' is currently listening to "' + string + '"' + " " + song_url)
                    db.write(string + '\n')
                except :
                    print("You have tweeted it before.")
                    sleep(60)
                    continue

        elif response.status_code == 204 and previous_response != 204:
            print("Not playing at the moment")
            sleep(60)
        elif response.status_code == 401 :        
            data = st.start_session(sys.argv[1], sys.argv[2])
            token = data[0]
            expiration_date = data[1]
            sleep(60)
            

        counter += 1
        previous_response = response.status_code
        sleep(60)

if __name__ == "__main__":
    songs = init()
    try :
        db = open("db.txt", "a")
        runner(db, songs)
    except KeyboardInterrupt:
        db.close()
        print("  Bye!")