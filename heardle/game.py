import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('game', __name__)

@bp.route('/search', methods=('GET', 'POST'))
def register():
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
    return render_template('game/play.html', playlist_id=playlist_id)