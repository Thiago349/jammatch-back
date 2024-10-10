import os
import requests
import json

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
SPOTIFY_REDIRECT_URI = os.environ['SPOTIFY_REDIRECT_URI']

SPOTIFY_BASE_URL = "https://api.spotify.com"

class SpotifyClient:
    def authenticate(code):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "code": code,
            "redirect_uri": SPOTIFY_REDIRECT_URI,
            "grant_type": 'authorization_code',
            "client_id": SPOTIFY_CLIENT_ID,
            "client_secret": SPOTIFY_CLIENT_SECRET
        }

        response = requests.post(f"https://accounts.spotify.com/api/token", data=data, headers=headers)
        auth = json.loads(response.text)
        
        if response.status_code == 200:
            return auth
        return None


    def refresh(refreshToken):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "refresh_token": refreshToken,
            "grant_type": 'refresh_token',
            "client_id": SPOTIFY_CLIENT_ID,
            "client_secret": SPOTIFY_CLIENT_SECRET
        }

        response = requests.post(f"https://accounts.spotify.com/api/token", data=data, headers=headers)
        auth = json.loads(response.text)
        if response.status_code == 200:
            return auth
        return None
    

    def getGenres(headers):
        response = requests.get(f"{SPOTIFY_BASE_URL}/v1/recommendations/available-genre-seeds", headers=headers)
        genreSeeds = json.loads(response.text)

        if response.status_code != 200:
            print(genreSeeds)
            return None
        return json.loads(response.text)
    

    def getSelf(headers):
        response = requests.get(f"{SPOTIFY_BASE_URL}/v1/me", headers=headers)
        self = json.loads(response.text)

        if response.status_code != 200:
            print(self)
            return None
        return json.loads(response.text)