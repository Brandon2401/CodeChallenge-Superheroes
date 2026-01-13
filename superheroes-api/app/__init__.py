from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import api
from .config import Config
from .mail import mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    mail.init_app(app)

    app.register_blueprint(api)

    return app
