from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower

api = Blueprint("api", __name__)
