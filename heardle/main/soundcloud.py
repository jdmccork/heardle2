from sclib import SoundcloudAPI, Track, Playlist

def init_soundcloud_client():
    # Create a Spotify client
    return SoundcloudAPI()

def get_playlist(playlist):
    api = init_soundcloud_client()

    # Retrieve the playlist
    # playlist = api.playlist(playlist_id)

    playlist = api.resolve(playlist)
    #'https://soundcloud.com/jess-mccorkindale/sets/good-songs'
    return playlist

def get_track(track_url):
    api = init_soundcloud_client()

    # Retrieve the tracks
    track = api.resolve(track_url)
    return track
    