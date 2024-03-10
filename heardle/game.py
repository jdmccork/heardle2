import functools
import random

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import spotify

bp = Blueprint('game', __name__)

@bp.route('/search', methods=('GET', 'POST'))
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

@bp.route('/play/<string:playlist_id>', methods=('GET', 'POST'))
def play(playlist_id):
    playlist = spotify.retrieve_playlist(playlist_id)
    track = None
    while not track or track['items'][0]['track']['preview_url'] == None:
        track = spotify.retrieve_playlist_track(playlist_id, limit=1, offset=random.randrange(0, playlist['tracks']['total']))
    return render_template('game/play.html', playlist=playlist, track=track)




"""
PlaylistID = 1CZb3d0AulrYDaJKi4636r
Useful api links
playlist_cover_image(playlist_id)
"""