
from flask import Blueprint, jsonify, Flask
from flask_sqlalchemy import SQLAlchemy
from models import Planets


planets_bp= Blueprint('planets1',__name__)

@planets_bp.route("/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = Planets.query.get_or_404(planet_id)
    return jsonify(planet.serialize())

@planets_bp.route("/get-all-planets", methods=["GET"])
def get_all_planets():
    planets = Planets.query.all()
    return jsonify([planet.serialize() for planet in planets])
    

@planets_bp.route("/create",methods=["POST"])
def create_planets():
    return "planetas creado",201