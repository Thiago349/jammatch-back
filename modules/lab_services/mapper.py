class LabServicesMapper:
    def spotifyTrackToTrackDTO(track):
        trackDTO = {
            'id': track['id'],
            'name': track['name'],
            'artists': [artist['name'] for artist in track['artists']],
            'album': track['album']['name'],
            'durationMs': track['duration_ms']
        }
        return trackDTO
    

    def spotifyParamsToParamsDTO(params):
        paramsDTO = {}
        for key, value in params.items():
            parts = key.split('_')
            paramsDTO[parts[1]] = value
        return paramsDTO
    

    def playlistDTO(paramsDTO, trackDTOs, type, name):
        playlistDTO = {
            "name": name,
            "parameters": paramsDTO,
            "tracks": trackDTOs,
            "type": type
        }
        return playlistDTO