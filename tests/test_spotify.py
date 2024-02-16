import pytest
from unittest.mock import patch
from heardle.util import spotify

def test_mocking_spotipy():
    """
    Tests mocking the Spotify client to retrieve a playlist
    """
    playlist_id = 'your_playlist_id'
    expected_playlist = {
        'id': 'your_playlist_id',
        'name': 'Your Playlist',
        'tracks': [
            {'id': 'track1', 'name': 'Track 1'},
            {'id': 'track2', 'name': 'Track 2'},
            {'id': 'track3', 'name': 'Track 3'}
        ]
    }

    with patch('heardle.util.spotify.init_spotify_client') as mock_init_spotify_client:
        mock_spotify_client = mock_init_spotify_client.return_value
        mock_spotify_client.playlist.return_value = expected_playlist

        playlist = spotify.retrieve_playlist(playlist_id)

        assert playlist == expected_playlist
        mock_spotify_client.playlist.assert_called_with(playlist_id)

def test_playlist_retrevial():
    """
    Tests retrieving a playlist from Spotify
    """
    playlist_id = '11jaQcBfdJl7qlra8HJwYF'
    playlist = spotify.retrieve_playlist(playlist_id)

    assert playlist['id'] == playlist_id
    assert playlist['name'] == 'Distractions music share'
    assert playlist['tracks']['total'] == 15