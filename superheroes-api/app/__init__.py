from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import api
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
   
   

    app.register_blueprint(api)

    return app
