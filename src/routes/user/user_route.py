#blueprints

from flask import Blueprint, jsonify
from models import User, Favorite

user_bp = Blueprint('user1',__name__)

@user_bp.route("/", methods=["GET"])
def base_function():
    return "esta funcionando",200

@user_bp.route("/create",methods=["POST"])
def create_user():
    return "Usuario creado",201

@user_bp.route("/get-all-users", methods=["GET"])
def get_all_user():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])


@user_bp.route("/favorites", methods=["GET"])
def get_favorites_users():
    favorites = Favorite.query.all()
    return jsonify([favorite.serialize() for favorite in favorites])

@user_bp.route("/<int:favorite_id>", methods=["GET"])
def get_favorite(favorite_id):
    favorite = Favorite.query.get_or_404(favorite_id)
    return jsonify(favorite.serialize())

