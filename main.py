import eel
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
topartists = []  # top ten artists
topsongs = []
topcounter = []
time_of_listen = []
display_artists = []
time_icon = ""
total_time = 0
top_artists_complete = 0
graph_int = 0

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
def get_user_image():
    token = getToken()
    sp = spotipy.Spotify(auth=token)
    user = sp.user("12178010763")
    userImageURL = sp.user("12178010763").get('images')
    userImage = userImageURL[0].get('url')
    return '<img src="' + userImage + '" width="220" height="220">'


@eel.expose
def get_user_info():
    token = getToken()
    sp = spotipy.Spotify(auth=token)
    userImageURL = sp.user("12178010763").get('images')
    userName = sp.user("12178010763").get('display_name')
    userURLDict = sp.user("12178010763").get('external_urls')
    userURL = userURLDict.get('spotify')
    userTopSong = topsongs[0]
    info = '<b>User:</b> ' + userName + " " + '<a href="' + userURL + '"><img src="Spotify_Icon_RGB_Green.png" width="30" height="30"></a>' + \
           '<br><b>Top Artist:</b> ' + topartists[0] + '<br><b>Top Song:</b> ' + topsongs[0] + '<br><b>Most Active During: </b> ' + time_icon \
           + '<br><b>Total Time Listened:</b> ' + total_time
    return info


@eel.expose
def top_artists_year():
    global top_artists_complete, topsongs
    top_artists_complete = 1

    YEAR = 2021

    artists = []
    tracks = []
    test = []
    num = []
    listens = np.array((10, 12), dtype=int)

    for item in streaming_history():
        if item.timestamp.year != YEAR:
            continue

        artists.append(item.artist)
        tracks.append((item.track, item.artist))

    for artist, counter in Counter(artists).most_common(10):
        print(f"{artist} [{counter}]")
        topartists.append(artist)
        topcounter.append(counter)

    for (track, artist), counter in Counter(tracks).most_common(20):
        print(f"{track} by {artist} [{counter}]")
        test.append(str(track + " - " + artist))
        num.append(counter)

    print(topartists)
    topsongs = test
    time_song_listened_to()


def time_song_listened_to():
    YEAR = 2021
    global time_icon, total_time

    morning = 0
    afternoon = 0
    evening = 0
    time_total = 0

    for item in streaming_history():
        if item.timestamp.year != YEAR:
            continue

        time = item.timestamp.time().strftime("%H:%M")
        time_of_listen.append(time)
        time_total += 1
        total_time += item.ms_played

    for item in time_of_listen:
        if "04:00" <= item < "12:00":
            morning += 1
        elif "12:00" <= item < "20:00":
            afternoon += 1
        else:
            evening += 1


    times = [morning, afternoon, evening]
    largest_time = times[0]
    time_period = 0
    for num in times:
        if num > largest_time:
            largest_time = num
            time_period += 1

    if time_period == 0:
        time_icon = '<img src="morningicon.png" id="normal"><img src="afternoonicon.png" id="faded"><img src="nighticon.png" id="faded">'
    elif time_period == 1:
        time_icon = '<img src="morningicon.png" id="faded"><img src="afternoonicon.png" id="normal"><img src="nighticon.png" id="faded">'
    else:
        time_icon = '<img src="morningicon.png" id="faded"><img src="afternoonicon.png" id="faded"><img src="nighticon.png" id="normal">'

    total_time = f"{total_time/1000/60/60:0.2f} hours"
    print(total_time)
    print(time_icon)
    print("Big: " + str(largest_time))


@eel.expose
def userTrackStuff():
    global display_artists
    token = getToken()
    sp = spotipy.Spotify(auth=token)
    track = sp.search(q='artist:' + "Nasty Cherry" + ' track:' + "Brain Soup", type="track")
    track_dict = track['tracks']['items'][0]['id']
    features = sp.audio_features(track_dict)
    temp_string = ""
    counter = 0
    for x in topartists:
        artist_search = sp.search(q='artist:' + topartists[counter])

        if topartists[counter] == "CHUNG HA":
            artist_info = sp.artist("2PSJ6YriU7JsFucxACpU7Y")
            artist_img_url = artist_info['images'][0]['url']
        elif topartists[counter] == "ROSÉ":
            artist_info = sp.artist("3eVa5w3URK5duf6eyVDbu9")
            artist_img_url = artist_info['images'][0]['url']
        else:
            artist_id = artist_search['tracks']['items'][0]['artists'][0]['id']
            artist_info = sp.artist(artist_id)
            artist_img_url = artist_info['images'][0]['url']

        print(artist_img_url)
        temp_string += f'<div class="{topartists[counter]}" id="artist_row">' + f'<img src="{artist_img_url}" id="artist">' +\
                       " " + topartists[counter] + "     " + f'<span id="listen_count">{str(topcounter[counter])} Plays</span>' + \
                       "<br>" + f'<div class="artist{str(counter)}">' + f'{get_artist_graphs(counter)}' + '</div></div>'
        display_artists.append(temp_string)
        counter += 1

    return temp_string

@eel.expose
def display_user_info():
    temp = '<center><img src="topsongs.png"><br><img src="streamspertime.png"></center>'
    return temp

@eel.expose
def get_artist_graphs(tempInt):

    temp = f'<center><img src="songplays{topartists[tempInt]}.png">' + f'<img src="month{topartists[tempInt]}.png">' + f'<img src="songpie{topartists[tempInt]}.png"></center>'
    return temp


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

    if top_artists_complete == 0:
        top_artists_year()

    return userToken


eel.start("index.html")
