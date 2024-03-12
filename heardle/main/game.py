import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
)
from flask_socketio import emit
from . import main
from . import soundcloud
from .. import socketio
import tempfile


@socketio.on('my event')
def my_event(message):
    print("test")
    emit('my response', {'data': 'got it!'})

@socketio.on("search")
def search_playlist(playlistName):
    print(playlistName)
    playlist = soundcloud.search_playlist(playlistName)
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
    playlist = soundcloud.get_playlist(playlist_id)

    track = random.choice(playlist.tracks)
    print(track)
    #Get length of playlist
    return render_template('game/play.html', playlist=playlist, track=track)


@main.route('/test')
def test():
    playlist = soundcloud.get_playlist("test")

    track = random.choice(playlist.tracks)

    with tempfile.NamedTemporaryFile() as file:
        track.write_mp3_to(file)

        data = file.read(1024)
        while data:
            yield data
            data = file.read(1024)
                
        return Response(file, mimetype="audio/mpeg")


"""
Useful api links
playlist_cover_image(playlist_id)
"""