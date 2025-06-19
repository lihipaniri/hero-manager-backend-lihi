from flask_cors import CORS
from flask_socketio import SocketIO

from flask import Flask

from src.config import Config
from src.controllers.router import make_routes
from src.database.database import Base, engine


def create_app(config: Config = Config) -> Flask:
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(config)

    make_routes(app)

    Base.metadata.create_all(engine)

    return app
