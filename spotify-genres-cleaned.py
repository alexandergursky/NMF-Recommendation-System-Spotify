# This is working on sparse5 but has problems on sparse9
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import concurrent.futures

# Load data
master_df = pd.read_csv('spotify-sparse9.csv')

# Extracting a list of artist names
artist_list = master_df['artistname'].values.tolist()

# --------------------------------------------------
# Private Information
client_id = 'null'
client_secret = 'null'
# --------------------------------------------------

# Initialize Spotipy client
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# List of artist names
artists = artist_list  # ['Kendrick Lamar', 'Beyonce', 'Drake']

# Function to get genres for a single artist
def get_artist_genres(artist):
    results = sp.search(q=artist, type='artist')
    if len(results['artists']['items']) > 0:
        return set(results['artists']['items'][0]['genres'])
    else:
        return set()

# Get genres for each artist in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_artist_genres, artist) for artist in artists]
    results = [f.result() for f in futures]

# Combine all genres into a single set
genres = set().union(*results)

print(len(genres))

# Terminal output:
# 2069