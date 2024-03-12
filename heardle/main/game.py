import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response, jsonify, stream_with_context
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
    # playlist = soundcloud.get_playlist(playlist_id)

    # randSeed = request.args.get('seed')
    # random.seed(randSeed)
    # track = random.choice(playlist.tracks)
    
    # print(track)
    #Get length of playlist
    return render_template('game/play.html')

@main.route('/test2')
def test2():
    playlist = soundcloud.get_playlist("test")

    randSeed = request.args.get('seed')
    random.seed(randSeed)
    track = random.choice(playlist.tracks)

    # Adds the track title and artist to the response
    response = {
        "title": track.title,
        "artist": track.artist,
        'url': track.permalink_url
    }

    return jsonify(response)
    

@main.route('/track')
def test():
    track_url = request.args.get('track_url')
    # track_url = "https://soundcloud.com/stealers-wheel/stuck-in-the-middle-with-you"
    print(track_url)
    track = soundcloud.get_track(track_url)

    def generate():
        with tempfile.NamedTemporaryFile() as file:
            track.write_mp3_to(file)

            data = file.read(1024)
            while data:
                yield data
                data = file.read(1024)

    return Response(stream_with_context(generate()), mimetype="audio/mpeg")


"""
Useful api links
playlist_cover_image(playlist_id)
"""