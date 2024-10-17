import random
from services.spotify.endpoints.client import SpotifyClient

class LabServicesService:
    def generateRamdomPlaylist(spotifyToken):
        randomParams = { 
            "seed_genres": ",".join(random.sample(["pop", "rock", "jazz", "classical", "hip-hop", "country", "blues", "reggae", "electronic", "folk", "soul", "metal"], 3)),
            "target_danceability": round(random.uniform(0.0, 1.0), 2),
            "target_energy": round(random.uniform(0.0, 1.0), 2),
            "target_acousticness": round(random.uniform(0.0, 1.0), 2),
            "target_instrumentalness": round(random.uniform(0.0, 1.0), 2),
            "target_liveness": round(random.uniform(0.0, 1.0), 2),
            "target_speechiness": round(random.uniform(0.0, 1.0), 2),
            "target_loudness": round(random.uniform(-60.0, 0.0), 2),
            "target_happiness": round(random.uniform(0.0, 1.0), 2)
        }
        formatedParams = {}
        for key, value in randomParams.items():
            parts = key.split('_')

            formatedParams[parts[1]] = value

        randomParams["limit"] = 10

        spotifyRecommendations = SpotifyClient.getSpotifyRecommendations(spotifyToken, randomParams)
        if "tracks" in spotifyRecommendations:
            recommendations = []
            for track in spotifyRecommendations['tracks']:
                trackInfo = {
                    'trackName': track['name'],
                    'trackId': track['id'],
                    'artists': [artist['name'] for artist in track['artists']],
                    'album': track['album']['name'],
                    'durationMs': track['duration_ms']
                }
                recommendations.append(trackInfo)

            playlist = {
                "parameters": formatedParams,
                "tracks": recommendations,
                "type": "SPOTIFY"
            }
        else:
            playlist = {
                "parameters": formatedParams,
                "tracks": "No recommendations found",
                "type": "SPOTIFY"
            }
        
        
        return playlist