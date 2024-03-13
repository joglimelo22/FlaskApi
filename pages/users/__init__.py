from flask import Blueprint, jsonify, request

from classes.main.users import USERS


users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users", methods=["GET"])
def get():
    return USERS.GET()


@users_blueprint.route("/users", methods=["POST"])
def post():
    name = request.get_json()["name"]
    usersname = request.get_json()["usersname"]
    password = request.get_json()["password"]
    permissionID = request.get_json()["permissionID"]
    
    return USERS.POST(name, usersname, password, permissionID)