import eel
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

eel.init("static_web_folder")


@eel.expose
def print_albums():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    sp2 = auth_manager.

    tbirdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

    results = sp.artist_albums(tbirdy_uri, album_type='album')
    albums = results['items']
    holder = ""

    userID = sp.user("12178010763")
    user = sp.user
    songs = user['items']

    while user['next']:
        results = sp.next(user)
        user.extend(songs['items'])

    for songList in songs:
        holder += songs['name']
        print(holder)

    return holder


eel.start("index.html")
