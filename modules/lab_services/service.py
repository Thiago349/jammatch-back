import random
from services.spotify.endpoints.client import SpotifyClient
from modules.lab_services.mapper import LabServicesMapper
from modules.spotify_services.mapper import SpotifyServicesMapper


class LabServicesService:
    def generateRandomPlaylist(spotifyToken, limit):
        randomParams = { 
            "seed_genres": ",".join(random.sample(["pop", "rock", "jazz", "classical", "hip-hop", "country", "blues", "reggae", "electronic", "folk", "soul", "metal", "disco", "funk", "indie", "punk", "bossanova", "samba", "sertanejo", "forro", "salsa", "ska", "grunge", "mpb", "pagode"], 2)),
            "target_danceability": round(random.uniform(0.0, 1.0), 2),
            "target_energy": round(random.uniform(0.0, 1.0), 2),
            "target_acousticness": round(random.uniform(0.0, 1.0), 2),
            "target_instrumentalness": round(random.uniform(0.0, 1.0), 2),
            "target_popularity": random.randint(0, 100),
            "target_happiness": round(random.uniform(0.0, 1.0), 2)
        }
        paramsDTO = LabServicesMapper.spotifyParamsToParamsDTO(randomParams)
        randomParams["limit"] = limit

        spotifyRecommendations = SpotifyClient.getSpotifyRecommendations(spotifyToken, randomParams)
        if spotifyRecommendations is not None:
            trackDTOs = []
            for track in spotifyRecommendations['tracks']:
                trackDTO = LabServicesMapper.spotifyTrackToTrackDTO(track)
                trackDTOs.append(trackDTO)

            playlistDTO = LabServicesMapper.playlistDTO(paramsDTO, trackDTOs, "SPOTIFY", None)
            return playlistDTO
        else:
            return None
    

    def generateCustomPlaylist(spotifyToken, customParams, playlistName, limit):
        spotifyParams = SpotifyServicesMapper.paramsDTOToSpotifyParams(customParams)
        print(customParams)
        spotifyParams["limit"] = limit

        spotifyRecommendations = SpotifyClient.getSpotifyRecommendations(spotifyToken, spotifyParams)
        if spotifyRecommendations is not None:
            trackDTOs = []
            for track in spotifyRecommendations['tracks']:
                trackDTO = LabServicesMapper.spotifyTrackToTrackDTO(track)
                trackDTOs.append(trackDTO)

            playlistDTO = LabServicesMapper.playlistDTO(customParams, trackDTOs, "SPOTIFY", playlistName)
            return playlistDTO
        else:
            return None