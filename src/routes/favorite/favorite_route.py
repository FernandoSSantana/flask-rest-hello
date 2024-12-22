
from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Favorite, Planets, User, People, db

favorites_bp = Blueprint('favorites',__name__)

@favorites_bp.route("/create",methods=["POST"])
def create_favorite():
    return "favorite creado",201

@favorites_bp.route("/<int:favorite_id>", methods=["GET"])
def get_favorite(favorite_id):
    favorite = Favorite.query.get_or_404(favorite_id)
    return jsonify(favorite.serialize())

@favorites_bp.route("/get-all-favorites", methods=["GET"])
def get_all_favorites():
    favorites = Favorite.query.all()
    return jsonify([favorite.serialize() for favorite in favorites])

@favorites_bp.route("/planet/<int:planet_id>", methods=["POST"])
def add_favorite_planet(planet_id):
    user = User.query.first()
    favorite_planet = Planets.query.get_or_404(planet_id)
    new_favorite = Favorite(planets_id=planet_id, user_id=user.id) 
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({
        "message": "Planet added to favorites",
        "planet": favorite_planet.serialize()
    }), 201 

@favorites_bp.route("/people/<int:people_id>", methods=["POST"])
def add_favorite_people(people_id):
    user = User.query.first()
    favorite_person = People.query.get_or_404(people_id)
    new_favorite = Favorite(people_id=people_id, user_id=user.id) 
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({
        "message": "People added to favorites",
        "people": favorite_person.serialize()
    }), 201 



@favorites_bp.route("/planet/<int:planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    user = User.query.first()
    favorite_planet = Favorite.query.filter_by(planets_id=planet_id, user_id=user.id).first()
    if not favorite_planet:
        return {"error": "Favorite planet not found"}, 404
    db.session.delete(favorite_planet)
    db.session.commit()
    return {"message": "Favorite planet deleted successfully"}, 200


@favorites_bp.route("/people/<int:people_id>", methods=["DELETE"])
def delete_people(people_id):
    user = User.query.first()
    favorite_person = Favorite.query.filter_by(people_id=people_id, user_id=user.id).first()
    if not favorite_person:
        return {"error": "favorite person not found"}, 200
    db.session.delete(favorite_person)
    db.session.commit()
    return jsonify({
        "message": "People deleted to favorites",
        "people": favorite_person.serialize()
    }), 200 