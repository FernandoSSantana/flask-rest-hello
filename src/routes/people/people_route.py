
from flask import Blueprint, jsonify
from models import People, User, db

people_bp = Blueprint('people1',__name__)

@people_bp.route("/<int:people_id>", methods=["GET"])
def get_person(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.serialize())

@people_bp.route("/get-all-people", methods=["GET"])
def get_all_people():
    people = People.query.all()
    return jsonify([person.serialize() for person in people])

@people_bp.route("/create",methods=["POST"])
def create_people():
    return "people creado",201

