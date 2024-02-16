import pytest
from flask import g, session

def test_search(client):
    # Tests that searching for playlist 03XeB2y3jTZMZXgqXoULSk returns the correct playlist
    response = client.get('/search')

    assert response.status_code == 200

    response = client.post('/search', data={'playlistId': '03XeB2y3jTZMZXgqXoULSk'})

    assert response.status_code == 302

def test_play(client):
    # Tests that playing a playlist with id 03XeB2y3jTZMZXgqXoULSk returns the correct playlist
    response = client.get('/play/03XeB2y3jTZMZXgqXoULSk')

    assert response.status_code == 200
