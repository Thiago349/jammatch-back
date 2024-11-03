genresDictionary = {
    'POP': "pop",
    'ROCK': "rock",
    'JAZZ': "jazz",
    'CLASSICAL': "classical",
    'HIP_HOP': "hip-hop",
    'COUNTRY': "country",
    'BLUES': "blues",
    'REGGAE': "reggae",
    'ELECTRONIC': "electronic",
    'FOLK': "folk",
    'SOUL': "soul",
    'METAL': "metal",
    'DISCO': "disco",
    'FUNK': "funk",
    'INDIE': "indie",
    'PUNK': "punk",
    'BOSSANOVA': "bossanova",
    'SAMBA': "samba",
    'SERTANEJO': "sertanejo",
    'FORRO': "forro",
    'SALSA': "salsa",
    'SKA': "ska",
    'GRUNGE': "grunge",
    'MPB': "mpb",
    'PAGODE': "pagode"
}


class SpotifyServicesMapper:
    def paramsDTOToSpotifyParams(params):
        paramsDictionary = { 
            'genres': "seed_genres",
            'danceability': "target_danceability",
            'energy': "target_energy",
            'acousticness': "target_acousticness",
            'instrumentalness': "target_instrumentalness",
            'popularity': "target_popularity",
            'loudness': "target_loudness",
            'happiness': "target_happiness"
        }

        spotifyParams = {}
        for param in params:
            if param in paramsDictionary:
                if param == 'genres':
                    genreCommaSeparated = ''
                    for genre in params[param]:
                        genreCommaSeparated += genresDictionary[genre]
                        if genre != params[param][-1]:
                            genreCommaSeparated += ','
                    spotifyParams[paramsDictionary[param]] = genreCommaSeparated
                else:
                    spotifyParams[paramsDictionary[param]] = params[param]

        
        return spotifyParams