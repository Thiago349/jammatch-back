from modules.users.controller import api as users_api
from modules.auth.controller import api as auth_api

def register_swagger_apis(api):
    api.add_namespace(users_api)
    api.add_namespace(auth_api)