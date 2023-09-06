import pandas as pd
import random

df = pd.read_csv("data/top_10000_1960-now.csv")

def discover():
    rng = random.randint(0, len(df))
    artist_name = df.loc[rng]['Artist Name(s)']
    song_name = df.loc[rng]['Track Name']
    return artist_name, song_name

def get_stats(artist_name, song_name):
    song = df[(df['Track Name'] == song_name) & (df['Artist Name(s)'] == artist_name)]
    image_url = song['Album Image URL'].iloc[0]
    return image_url


