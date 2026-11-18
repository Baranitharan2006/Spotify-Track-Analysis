
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Check Client ID length
client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
print("Client ID length:", len(client_id))

# Connect to Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"]
    )
)

# Test Spotify API
track = sp.track("3n3Ppam7vgaVa1iaRUc9Lp")

print("Authentication successful!")
print("Track:", track["name"])
print("Artist:", track["artists"][0]["name"])
