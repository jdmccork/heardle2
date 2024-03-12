from sclib import SoundcloudAPI, Track, Playlist

def init_soundcloud_client():
    # Create a Spotify client
    return SoundcloudAPI()

def get_playlist(playlist_id):
    api = init_soundcloud_client()

    # Retrieve the playlist
    # playlist = api.playlist(playlist_id)

    playlist = api.resolve('https://soundcloud.com/jess-mccorkindale/sets/good-songs')
    
    return playlist

def get_playlist_track(playlist_id, offset=0):
    api = init_soundcloud_client()

    # Retrieve the tracks
    track = api.playlist_tracks(playlist_id, limit=1, offset=offset)
    return track
    