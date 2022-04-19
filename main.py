import eel
import sys
import spotipy
import json
import base64
import numpy as np
import requests
import matplotlib.pyplot as plt
import spotipy.util as util
from collections import namedtuple
from datetime import datetime
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotipy import oauth2
from collections import Counter
Item = namedtuple("Item", ["artist", "track", "ms_played", "timestamp"])
userToken = ""
userImage = ""
userName = ""
userURL = ""


eel.init("static_web_folder")


@eel.expose
def streaming_history():
    print("Test")
    file = open("StreamingHistory0.json", "r+", encoding="utf-8")
    testJson = json.load(file)
    for item in testJson:
        if item.get("artistName") == "Unknown Artist":
            continue

        if item.get("trackName") == "Unknown Track":
            continue

        yield Item(
            artist=item.get("artistName"),
            track=item.get("trackName"),
            ms_played=item.get("msPlayed", 0),
            timestamp=datetime.strptime(
                item["endTime"],
                "%Y-%m-%d %H:%M"
            )
        )


@eel.expose
def try_func():

    YEAR = 2021

    topartists = []
    artists = []
    listens = np.array((10,12),dtype =int)


    for item in streaming_history():
        if item.timestamp.year != YEAR:
            continue

        artists.append(item.artist)


    for artist, counter in Counter(artists).most_common(10):
        print(f"{artist} [{counter}]")
        topartists.append(artist)


    topartists = list(set(topartists))
    print(topartists)

    return topartists


@eel.expose
def get_user_image():
    token = getToken()
    sp = spotipy.Spotify(auth=token)
    user = sp.user("12178010763")
    userImageURL = sp.user("12178010763").get('images')
    userImage = userImageURL[0].get('url')
    return '<img src="' + userImage + '" width="160" height="160">'

@eel.expose
def get_user_info():
    token = getToken()
    sp = spotipy.Spotify(auth=token)
    userImageURL = sp.user("12178010763").get('images')
    userName = sp.user("12178010763").get('display_name')
    userURLDict = sp.user("12178010763").get('external_urls')
    userURL = userURLDict.get('spotify')
    return 'User: ' + userName + " " + '<a href="' + userURL + '"><img src="Spotify_Icon_RGB_Green.png" width="10" height="10"></a>'

def userTrackStuff():
    track = sp.search(q='artist:' + "Nasty Cherry" + ' track:' + "Brain Soup", type="track")
    track_dict = track['tracks']['items'][0]['id']
    features = sp.audio_features(track_dict)



def getToken():
    SPOTIPY_CLIENT_ID = '288dfaa928f04c69a45267bd1ba69fe2'
    SPOTIPY_CLIENT_SECRET = 'd308118dc2b84a16a4cc87d36f491d62'
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    message = f"{SPOTIPY_CLIENT_ID}:{SPOTIPY_CLIENT_SECRET}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"
    data['json'] = True
    data['scope'] = 'user-read-recently-played'
    r = requests.post(url=url, headers=headers, data=data)
    userToken = r.json()['access_token']

    return userToken

eel.start("index.html")
