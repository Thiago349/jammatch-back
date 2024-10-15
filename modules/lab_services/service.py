import random
from services.spotify.endpoints.client import SpotifyClient

class LabServicesService:
    def generateRamdomPlaylist(spotifyToken):
        randomParams = {
            "limit": random.randint(1, 100), 
            "seed_genres": ",".join(random.sample(["pop", "rock", "jazz", "classical", "hip-hop", "country", "blues", "reggae", "electronic", "folk", "soul", "metal"], 3)),
            "target_danceability": round(random.uniform(0.0, 1.0), 2),
            "target_energy": round(random.uniform(0.0, 1.0), 2),
            "target_valence": round(random.uniform(0.0, 1.0), 2),
            "target_acousticness": round(random.uniform(0.0, 1.0), 2),
            "target_instrumentalness": round(random.uniform(0.0, 1.0), 2),
            "target_liveness": round(random.uniform(0.0, 1.0), 2),
            "target_speechiness": round(random.uniform(0.0, 1.0), 2),
            "target_tempo": random.randint(60, 200),
            "min_popularity": random.randint(0, 50),
            "max_popularity": random.randint(50, 100),
            "target_duration_ms": random.randint(120000, 300000),
            "target_loudness": round(random.uniform(-60.0, 0.0), 2),
            "target_key": random.randint(0, 11),
            "target_mode": random.randint(0, 1),
            "target_time_signature": random.randint(3, 7),
            "target_happiness": round(random.uniform(0.0, 1.0), 2),
            "target_danceability": round(random.uniform(0.0, 1.0), 2),
            "target_energy": round(random.uniform(0.0, 1.0), 2),
            "target_loudness": round(random.uniform(-60.0, 0.0), 2),
            "target_instrumentalness": round(random.uniform(0.0, 1.0), 2),
            "target_speechiness": round(random.uniform(0.0, 1.0), 2),
            "target_liveness": round(random.uniform(0.0, 1.0), 2),
            "target_tempo": random.randint(60, 180)
        }
        spotifyRecommendations = SpotifyClient.getSpotifyRecommendations(spotifyToken, randomParams)
        print(randomParams)
        return spotifyRecommendations