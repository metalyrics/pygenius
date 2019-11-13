import requests

import utils.process_lyrics as pl

print(pl.process_lyrics('a'))
def get_song_path(query, access_token):
    song = search_song(query, access_token)
    return song['path']

def search_song(query, access_token):
    BASE_PATH = 'https://api.genius.com'
    options = {
        'access_token': access_token,
        'q': query
    }
    response = requests.get(BASE_PATH + '/search', options).json()
    return response['response']['hits'][0]['result']