import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def init_spotify_client():
    # Create a Spotify client
    client_credentials_manager = SpotifyClientCredentials()
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def retrieve_playlist(playlist_id):
    sp = init_spotify_client()

    # Retrieve the playlist
    playlist = sp.playlist(playlist_id)
    
    return playlist

def retrieve_playlist_track(playlist_id, limit=1, offset=0):
    sp = init_spotify_client()

    # Retrieve the tracks
    tracks = sp.playlist_tracks(playlist_id, limit=limit, offset=offset)
    return tracks
    