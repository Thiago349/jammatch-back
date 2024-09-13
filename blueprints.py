from modules.auth.controller import api as auth_api
from modules.users.controller import api as users_api
from modules.profiles.controller import api as profiles_api

def register_swagger_apis(api):
    api.add_namespace(auth_api)
    api.add_namespace(users_api)
    api.add_namespace(profiles_api)