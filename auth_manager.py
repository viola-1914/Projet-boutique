

import json
from models.utilisateur import Utilisateur

USERS_FILE = "data/users.json"

def charger_utilisateurs():
    with open(USERS_FILE, "r") as f:
        data = json.load(f)
    return data

def verifier_connexion(username, password):
    users = charger_utilisateurs()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return Utilisateur(user["username"], user["role"])
    return None
