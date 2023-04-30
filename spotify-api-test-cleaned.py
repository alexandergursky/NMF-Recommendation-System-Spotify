# This accepts the artist's name and outputs the generes associated. Don't edit this script it works.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'null'
client_secret = 'null'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_genres(artist_names):
    genres = []
    for name in artist_names:
        result = sp.search(q='artist:' + name, type='artist')
        if result['artists']['items']:
            artist_id = result['artists']['items'][0]['id']
            artist = sp.artist(artist_id)
            artist_genres = artist['genres']
            genres.extend(artist_genres)
    return list(set(genres))

artist_names = ['Kendrick Lamar', 'Drake', 'J. Cole']
genres = get_artist_genres(artist_names)
print(genres)
# ['canadian pop', 'toronto rap', 'canadian hip hop', 'conscious hip hop', 'hip hop', 'north carolina hip hop', 'pop', 'rap', 'west coast rap']

# ---------------
# spotify-sparse5.csv
# Terminal Output: 2072
