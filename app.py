import serverless_wsgi
from flask import Blueprint, Flask, Response
from flask_restx import Api
from alchemy import Base, engine
from flask_cors import CORS
from blueprints import register_swagger_apis

app = Flask(__name__)
CORS(app)

app.logger.setLevel(20)
app.config["RESTX_MASK_HEADER"] = None
app.config["RESTX_MASK_SWAGGER"] = None
blueprint = Blueprint("api", __name__)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] =  '*'
    
    return response

api = Api(
    blueprint,
    title="Jammatch HUB API",
    version="1.0",
    description="",
)

register_swagger_apis(api)
app.register_blueprint(blueprint)

Base.metadata.create_all(bind=engine)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

if __name__ == "__main__":
    app.run(debug=True)