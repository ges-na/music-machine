import os
import unittest

from app import app, db
from views import *
from . import models

TEST_DB = 'test.db'

#testing ssh#

class BaseTest(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        create_fixtures()

    # executed after each test
    def tearDown(self):
        pass

    @property
    def band_data(self):
        return [
            {
                'name': 'ariel pink',
                'albums': [
                    {
                        'name': 'pom pom',
                        'songs': 10,
                    },
                ]
            },{
                'name': 'aphex twin',
                'albums': [
                    {
                        'name': 'druqs',
                        'songs': 7,
                    },
                ]
            },{
                'name': 'baroness',
                'albums': [
                    {
                        'name': 'red',
                        'songs': 8,
                    },{
                    'name': 'blue',
                    'songs': 9,
                    },
                ]
            },
        ]

    def create_fixtures(self):
        for band_data in self.band_data:
            band_instance = Band(name=band_data['name'])
            db.session.add(band_instance)
            for album_data in band_data['albums']:
                album_instance = Album(name=album_data['name'])
                db.session.add(album_instance)
                number_of_songs = album_data['songs']
                for track_number in range(1, number_of_songs):
                    song_instance = Song(name='track_{}'.format(track_number))
                    db.session.add(song_instance)
        db.session.commit()

###############
#### tests ####
###############

class ViewTest(BaseTest):

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    
if __name__ == "__main__":
    unittest.main()
