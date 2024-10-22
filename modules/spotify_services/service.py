import requests
from services.spotify.endpoints.client import SpotifyClient

class CreatePlaylistService:
    def createPlaylist(spotifyToken, userId, playlistName, tracks):

        newPlaylist = SpotifyClient.postPlaylist(spotifyToken, userId, playlistName)
        
        print(newPlaylist)
        playlistId = newPlaylist['id']

        uris = [f"spotify:track:{track_id}" for track_id in tracks]

        addTracks = SpotifyClient.postPlaylistTracks(spotifyToken, playlistId, uris)

        return {
            "id": playlistId
        }
        