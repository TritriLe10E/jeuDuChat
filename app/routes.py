from app import app
from app import sql_select, sql_insert, sql_delete, sql_update
from flask import request
from flask import jsonify


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    #requête pour récupérer les joueurs
    request_sql = f'''SELECT players_id, players_pseudo 
    FROM players'''

    #on exécute la requete
    data = sql_select(request_sql)

    #on print le résultat de la requête
    print(data)

    #on parcourt le résultat
    for player in data:
        #on récupère l'id du joueur
        player_id = player["players_id"]

        #requête pour récupérer les chats d'un joueur
        request_sql = f'''SELECT * FROM cats 
        JOIN rooms ON rooms.rooms_id = cats.rooms_id 
        WHERE rooms.players_id = {player_id}'''

        cats = sql_select(request_sql)
        print(f'''CHATS DU JOUEUR {player_id} : \n''')
        print(len(cats))

        #on ajoute le nombre de chats (le nombre d'objets dans la liste renvoyée par le serveur) au player actuel
        player["cats_count"] = len(cats)

    #on renvoie le résultat jsonifié
    return jsonify(data), 200

@app.route('/login', methods=['POST'])
def login():
    formulaire_connexion = (request.get_json())

    #on récupère l'email
    email = formulaire_connexion["email"]

    sql_request = f'''SELECT * FROM players WHERE players_email = "{email}"'''
    players_avec_cette_email = sql_select(sql_request)

    if len(players_avec_cette_email) == 0:
        #L'email existe
        return "l'e-mail n'existe pas", 404

    print(players_avec_cette_email)

    password = formulaire_connexion["password"]
    mot_de_passe = players_avec_cette_email[0]["players_password"]
    id_player = players_avec_cette_email[0]["players_id"]
    dictionnary = {"id" : id_player}
    print(players_avec_cette_email)
    if password == mot_de_passe:
        return jsonify(dictionnary), 200
    else:
        return "Connexion impossible", 404




@app.route('/signup', methods=['POST'])
def sign_up():
    #on récupère le json envoyé par le client
    formulaire_inscription = (request.get_json())

    #on récupère l'email
    email = formulaire_inscription["email"]

    #on check si l'email existe, si oui on envoie une erreur
    sql_request = f'''SELECT * FROM players WHERE players_email = "{email}"'''

    players_avec_cette_email = sql_select(sql_request)

    if len(players_avec_cette_email) > 0:
        return "Email déjà existant", 503

    #on ajoute le joueur
    sql_request = f'''INSERT INTO players(players_pseudo, players_email, players_password)
    VALUES("{formulaire_inscription["pseudo"]}", 
    "{formulaire_inscription["email"]}", 
    "{formulaire_inscription["password"]}")'''

    sql_insert(sql_request)

    return "OK", 200


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

