import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response, jsonify, stream_with_context
)
from flask_socketio import emit
from . import main
from . import soundcloud
from .. import socketio
# from .. import mysql
import tempfile
import json


@socketio.on('my event')
def my_event(message):
    print("test")
    emit('my response', {'data': 'got it!'})

@socketio.on("search")
def search_playlist(playlistName):
    print(playlistName)
    playlist = soundcloud.get_playlist(playlistName)
    emit('playlistResponse', {'playlist': playlist})

@main.route('/search', methods=['GET', 'POST'])
def loadPlaylist():
    if request.method == 'POST':
        playlist = request.form['playlist']
        error = None

        if not playlist:
            error = 'Playlist is required.'

        if error is None:
            session['playlist_url'] = playlist
            return redirect(url_for("main.play"))

        flash(error)

    return render_template('game/search.html')

@main.route('/play', methods=['GET', 'POST'])
def play():
    return render_template('game/play.html')

@main.route('/selectSong', methods=['GET'])
def selectSong():
    playlist_url = session['playlist_url'] 
    # playlist_url = request.args.get('playlist_url')
    playlist = soundcloud.get_playlist(playlist_url)
    # if 'playlist_url' in session:
    #     playlist = session['playlist_url']
    # else:
    #     playlist = soundcloud.get_playlist(playlist_url)
    #     for track in playlist.tracks:
    #         cursor = mysql.connection.cursor()
    #         cursor.execute(''' INSERT INTO playlist VALUES(%s,%s,%s)''',(track.title,track.artist,track.playlist_url))
    #         mysql.connection.commit()
    #         cursor.close()


    track = random.choice(playlist.tracks)

    # Adds the track title and artist to the response
    response = {
        "title": track.title,
        "artist": track.artist,
        'url': track.permalink_url
    }

    return jsonify(response)
    

@main.route('/track')
def track():
    track_url = request.args.get('track_url')
    
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