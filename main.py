import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n ")
bill_board_url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=bill_board_url)
web_content = response.text

soup = BeautifulSoup(web_content, "html.parser")
song_list = [song.get_text().split("\n")[1] for song in soup.find_all(name="h3",
                                                                      class_="c-title "
                                                                             "a-no-trucate "
                                                                             "a-font-primary-bold"
                                                                             "-s "
                                                                             "u-letter-spacing-0021 "
                                                                             "lrv-u-font-size-18@tablet "
                                                                             "lrv-u-font-size-16 u-line-height-125 "
                                                                             "u-line-height-normal@mobile-max "
                                                                             "a-truncate-ellipsis "
                                                                             "u-max-width-330 "
                                                                             "u-max-width-230@tablet-only")]
#
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                    client_secret=SPOTIFY_CLIENT_SECRET,
                                                    redirect_uri="http://example.com",
                                                    scope="playlist-modify-private",
                                                    show_dialog=True,
                                                    cache_path="token.txt")
                          )
user_id = spotify.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

new_playlist = spotify.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_id = new_playlist["id"]
add_track = spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris)
