from app import app
from app import sql_select, sql_insert, sql_delete, sql_update
from flask import request
from flask import jsonify


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return "Hello World", 200


@app.route('/login', methods=['POST'])
def login():
    return "Not implemented", 501


@app.route('/signup', methods=['POST'])
def sign_up():
    return "Not implemented", 501


@app.route('/users/<int:players_id>/rooms', methods=['GET', 'POST'])
def rooms_handling(players_id):
    if request.method == 'GET':
        return get_rooms_request(players_id)
    elif request.method == 'POST':
        return add_room_request(players_id, request.get_json())


def get_rooms_request(players_id):
    return "Not implemented", 501


def add_room_request(players_id, request_json):
    print(request_json)
    return add_room(players_id, request_json["position_x"], request_json["position_y"], request_json["seed"])


def add_room(players_id, pos_x, pos_y, seed):
    return "Not implemented", 501


@app.route('/users/<int:players_id>/rooms/<int:rooms_id>', methods=['DELETE'])
def delete_room(players_id, rooms_id):
    return "Not implemented", 501


@app.route('/cats', methods=['GET'])
def get_free_cats():
    return "Not implemented", 501


@app.route('/cats/<int:cats_id>', methods=['PATCH', 'DELETE'])
def update_cat(cats_id):
    return "Not implemented", 501

