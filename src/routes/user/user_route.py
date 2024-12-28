from flask import Blueprint, jsonify, request, Flask
from models import User, Favorite,db
from flask_bcrypt import Bcrypt

user_bp = Blueprint('user1',__name__)
bcrypt = Bcrypt()

@user_bp.route("/", methods=["GET"])
def base_function():
    return "esta funcionando",200
    

@user_bp.route("/create",methods=["POST"])
def create_user():
    return "Usuario creado",201

# @user_bp.route("/create",methods=["POST"])
# def create_user():
#     user_data = request.get_json()
#     new_user = User(**user_data)
#     new_user.password = Bcrypt.generate_password_hash(new_user.password).decode('utf-8')
#     # print(new_user.password)
#     db.session.add(new_user)
#     db.session.commit()
#     return "Usuario creado",200

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

