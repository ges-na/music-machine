from flask import render_template
from app import app
from models import *


@app.route('/')
def index():
    return render_template('index.html', bands=Band.query.order_by(Band.name).all())

@app.route('/<id>')
def discography(id):
    band = Band.query.get(id)
    return render_template('discography.html', band=band)

@app.route('/<band_id>/<album_id>')
def track_list(band_id, album_id):
    album = Album.query.get(album_id)
    return render_template('tracklist.html', album=album)
