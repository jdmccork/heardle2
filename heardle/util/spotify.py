import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def init_spotify_client():
    # Create a Spotify client
    client_credentials_manager = SpotifyClientCredentials()
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def retrieve_playlist(playlist_id):
    print("test")
    sp = init_spotify_client()

    # Retrieve the playlist
    playlist = sp.playlist(playlist_id)
    
    return playlist
    