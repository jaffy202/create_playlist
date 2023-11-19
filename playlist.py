import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'client id'
CLIENT_SECRET = 'client secret'
REDIRECT_URI = 'http://example.com'
user = 'username'


class Playlist:

    def __init__(self, songs_name, year, date):
        self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                              redirect_uri=REDIRECT_URI, show_dialog=True,
                                                              scope="playlist-modify-private", cache_path='token.txt',
                                                              username=user,))
        self.__user_id = self.__sp.current_user()['id']
        self.year = year
        self.date = date
        self.songs_names = songs_name
        self.__songs_uri = []
        for name in self.songs_names:
            self.__search_query = f'track:{name} year:{self.year}'
            self.__results = self.__sp.search(q=self.__search_query, type='track', limit=1)
            try:
                self.__song_uri = self.__results['tracks']['items'][0]['uri']
                self.__songs_uri.append(self.__song_uri)
            except IndexError:
                pass
        self.__create_playlist = self.__sp.user_playlist_create(user=self.__user_id,
                                                                name=f'{date} Billboard 100',
                                                                public=False)
        self.__playlist_id = self.__create_playlist['id']
        self.__sp.playlist_add_items(playlist_id=self.__playlist_id, items=self.__songs_uri, position=None)
