import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_socketio import emit
from . import main
from . import spotify
from .. import socketio


@socketio.on('my event')
def my_event(message):
    print("test")
    emit('my response', {'data': 'got it!'})

@socketio.on("search")
def search_playlist(playlistName):
    print(playlistName)
    playlist = spotify.search_playlist(playlistName)
    emit('playlistResponse', {'playlist': playlist})

@main.route('/search', methods=('GET', 'POST'))
def loadPlaylist():
    if request.method == 'POST':
        playlist_id = request.form['playlistId']
        error = None

        if not playlist_id:
            error = 'Playlist is required.'

        if error is None:
            return redirect(url_for("game.play", playlist_id=playlist_id))

        flash(error)

    return render_template('game/search.html')

@main.route('/play/<string:playlist_id>', methods=('GET', 'POST'))
def play(playlist_id):
    playlist = spotify.retrieve_playlist(playlist_id)
    track = None
    while not track or track['items'][0]['track']['preview_url'] == None:
        track = spotify.retrieve_playlist_track(playlist_id, limit=1, offset=random.randrange(0, playlist['tracks']['total']))
        #print track name and artist name
        print(track['items'][0]['track']['name'], ", ".join([x['name'] for x in track['items'][0]['track']['artists']]))
    #Get length of playlist
    return render_template('game/play.html', playlist=playlist, track=track)




"""
Useful api links
playlist_cover_image(playlist_id)
"""