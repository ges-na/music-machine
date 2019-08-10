
from app import db



class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return '<Band: {}>'.format(self.name)

    @property
    def albums_ordered(self):
        return self.albums.order_by(Album.name)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=True, nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'),
        nullable=True)
    band = db.relationship('Band',
        backref=db.backref('albums', lazy='dynamic'))

    def __repr__(self):
        return '<Album: {}>'.format(self.name)

    @property
    def tracklist(self):
        return self.songs.order_by(Song.name)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=True, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'),
        nullable=True)
    album = db.relationship('Album',
        backref=db.backref('songs', lazy='dynamic'))

    def __repr__(self):
        return '<Song: {}>'.format(self.name)
