import eel
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

eel.init("static_web_folder")


@eel.expose
def print_albums():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    tbirdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

    results = sp.artist_albums(tbirdy_uri, album_type='album')
    albums = results['items']
    holder = ""

    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        holder += album['name']
        print(holder)

    return holder


eel.start("index.html")
