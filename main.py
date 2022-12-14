import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth




question = input("which year do you want to travel to? type the date in format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{question}"

response = requests.get(URL)
webpage = response.text
list_of_titles = []
soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(id="title-of-a-story", class_="a-no-trucate")
for title in titles:
    list_of_titles.append(title.getText().strip("\n\t"))

client_id = 'f5af9d39167047b597f527cb753f9fb7'
client_secret = 'd29d9b6ba9a14892b6affc8cf9c31340'
redirect = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]
song_uris = []
year = question.split("-")[0]
for song in list_of_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard Top Tracks", public=False, description="Top tracks from bank in the dayz")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
