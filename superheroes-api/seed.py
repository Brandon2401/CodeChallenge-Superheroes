from app import create_app
from app.models import db, Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
