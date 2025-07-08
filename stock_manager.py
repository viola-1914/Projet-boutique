# -*- coding: utf-8 -*-
import json

FICHIER_STOCK = "stock.json"

def sauvegarder_produits(produits):
    data = [
        {
            "nom": p.nom,
            "prix": p.prix,
            "stock_disponible": p.stock_disponible,
            "stock_limite": p.stock_limite
        }
        for p in produits
    ]
    with open(FICHIER_STOCK, "w") as f:
        json.dump(data, f)

def charger_produits():
    from models.produit import produit
    produits = []
    try:
        with open(FICHIER_STOCK) as f:
            data = json.load(f)
            for d in data:
                p = produit(d["nom"], d["prix"], d["stock_disponible"], d["stock_limite"])
                p.ajouter_enboutique()
                produits.append(p)
    except FileNotFoundError:
        pass
    return produits

