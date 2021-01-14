#!/usr/bin/env python3
import spotipy
import yaml
import spotipy.util as util
from pprint import pprint

def load_config():
    global user_config
    stream = open('config.yaml')
    user_config = yaml.load(stream)

def get_top_25():
    tracks = []

    # make spotify call
    results = sp.current_user_top_tracks(limit=25, offset=0, time_range='short_term')
    for track in results['items']:
        tracks.append(track['id'])

    # add to playlist
    sp.user_playlist_replace_tracks(user_config['username'], user_config['playlist_id'], tracks)

if __name__ == '__main__':
    global sp
    global user_config
    load_config()

    token = util.prompt_for_user_token(user_config['username'], scope='user-top-read,playlist-modify-private,playlist-modify-public', client_id=user_config['client_id'], client_secret=user_config['client_secret'], redirect_uri=user_config['redirect_uri'])
    if token:
        sp = spotipy.Spotify(auth=token)
        get_top_25()
    else:
        pprint("Can't get token for", user_config['username'])
