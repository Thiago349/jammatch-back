class SpotifyServicesMapper:
    def paramsDTOToSpotifyParams(params):
        paramsDictionary = { 
            'genres': "seed_genres",
            'danceability': "target_danceability",
            'energy': "target_energy",
            'acousticness': "target_acousticness",
            'instrumentalness': "target_instrumentalness",
            'loudness': "target_loudness",
            'happiness': "target_happiness"
        }

        spotifyParams = {}
        for param in params:
            if param in paramsDictionary:
                spotifyParams[paramsDictionary[param]] = params[param]
        
        return spotifyParams