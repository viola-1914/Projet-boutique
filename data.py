from models.produit import produit

produits = [
    produit("savon caribou", 350, 50, 60),
    produit("lait", 400, 10, 20),
    produit("mil", 700, 20, 50)
]

for p in produits:
    p.ajouter_enboutique()
    