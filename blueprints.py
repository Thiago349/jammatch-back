from modules.users.controller import api as users_api

def register_swagger_apis(api):
    api.add_namespace(users_api)