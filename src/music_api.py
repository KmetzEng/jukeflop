"""
music_api

module responsible for all Spotify API activity
uses the spotipy library
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class MusicAPI():
    """
    MusicAPI
    """
    def __init__(self):
        self.spot = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def test_api(self, band):
        """
        Quick test for functionality of the Spotify API
        """
        result = self.spot.search(q=band, limit=20)
        for idx, track in enumerate(result['tracks']['items']):
            print(idx, track['name'])
