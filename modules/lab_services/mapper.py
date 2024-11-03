genresDictionary = {
    "pop": 'POP',
    "rock": 'ROCK',
    "jazz": 'JAZZ',
    "classical": 'CLASSICAL',
    "hip-hop": 'HIP_HOP',
    "country": 'COUNTRY',
    "blues": 'BLUES',
    "reggae": 'REGGAE',
    "electronic": 'ELECTRONIC',
    "folk": 'FOLK',
    "soul": 'SOUL',
    "metal": 'METAL',
    "disco": 'DISCO',
    "funk": 'FUNK',
    "indie": 'INDIE',
    "punk": 'PUNK',
    "bossanova": 'BOSSANOVA',
    "samba": 'SAMBA',
    "sertanejo": 'SERTANEJO',
    "forro": 'FORRO',
    "salsa": 'SALSA',
    "ska": 'SKA',
    "grunge": 'GRUNGE',
    "mpb": 'MPB',
    "pagode": 'PAGODE'
}


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
            if key == 'seed_genres':
                spotifyGenresList = value.split(',')
                genresList = []
                for genre in spotifyGenresList:
                    genresList.append(genresDictionary[genre])
                genresDictionary
                paramsDTO[parts[1]] = genresList
            else:
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