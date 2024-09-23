from modules.auth.controller import api as auth_api
from modules.users.controller import api as users_api
from modules.profiles.controller import api as profiles_api
from modules.roles.controller import api as roles_api
from modules.role_attachments.controller import api as role_attachments_api
from modules.spotify.controller import api as spotify_api
from modules.spotify_attachments.controller import api as spotify_attachments_api

def register_swagger_apis(api):
    api.add_namespace(auth_api)
    api.add_namespace(users_api)
    api.add_namespace(profiles_api)
    api.add_namespace(roles_api)
    api.add_namespace(role_attachments_api)
    api.add_namespace(spotify_api)
    api.add_namespace(spotify_attachments_api)