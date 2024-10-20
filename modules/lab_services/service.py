import random
from services.spotify.endpoints.client import SpotifyClient
from modules.lab_services.mapper import LabServicesMapper

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
        paramsDTO = LabServicesMapper.spotifyParamsToDTO(randomParams)

        randomParams["limit"] = 10

        spotifyRecommendations = SpotifyClient.getSpotifyRecommendations(spotifyToken, randomParams)
        if spotifyRecommendations is not None:
            trackDTOs = []
            for track in spotifyRecommendations['tracks']:
                trackDTO = LabServicesMapper.spotifyTrackToDTO(track)
                trackDTOs.append(trackDTO)

            playlist = {
                "parameters": paramsDTO,
                "tracks": trackDTOs,
                "type": "SPOTIFY"
            }
            return playlist
        else:
            return None
        
        