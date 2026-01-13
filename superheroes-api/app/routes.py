from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower

api = Blueprint("api", __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([h.to_dict() for h in heroes]), 200

@api.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "power": hp.power.to_dict()
            }
            for hp in hero.hero_powers
        ]
    }), 200

@api.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([p.to_dict() for p in powers]), 200

@api.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

