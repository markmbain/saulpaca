from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS


def create_app():
    load_dotenv()  # Load environment variables from .env
    app = Flask(__name__)
    CORS(app)

    with app.app_context():
        from . import routes

        app.register_blueprint(routes.app)

    return app
