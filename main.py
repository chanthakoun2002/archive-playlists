from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri=os.getenv('REDIRECT_URI'),
    scope=os.getenv('SCOPE'),
    cache_path=".spotify_cache"
))

# user = sp.current_user()
# print(f"Logged in as: {user['display_name']}")

playlist_id = input("Enter Playlist Link (Or Enter Playlist ID)").strip()


#handles link into id
if "spotify.com" in playlist_id:
    parts = playlist_id.split("/")
    playlist_id = parts[-1].split("?")[0] #gets the last val which will be the id

# fetch and extract playlist name
print(playlist_id)

try:
    playlist = sp.playlist(playlist_id)
    playlist_name = playlist["name"]
    print("Exporting: " + playlist_name)
except Exception as e:
    print("Error fetching playlist: ", e)
    exit()
