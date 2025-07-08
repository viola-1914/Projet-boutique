from models import produit, Utilisateur, Vente, Statistique

savon = produit("savon", 350, 2, 50)
lait = produit("marsa", 500, 15, 30)

savon.ajouter_enboutique()
lait.ajouter_enboutique()
savon.approvisionner(5)

print(savon)

user = Utilisateur("gunu", "475kj", "45op", "vendeur")
print(user)

vendeur1 = Vente(user)

vendeur1.ajouter_article(savon, 3)
vendeur1.ajouter_article(lait, 3)
vendeur1.facture()
vendeur1.facture()
print(savon)

stas = Statistique()
stas.enregistre_vente(vendeur1)
stas.total_ventes()

vendeur1.ajouter_article(savon, 1)
