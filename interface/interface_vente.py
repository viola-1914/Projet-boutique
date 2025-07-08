import tkinter as tk
from data import produits
from models.vente import Vente
import sys


# ➜ Récupérer nom vendeur depuis l'argument
vendeur_nom = sys.argv[1] if len(sys.argv) > 1 else "Vendeur inconnu"


#vendeur_nom = "kembou"
vendeur1 = Vente(vendeur_nom)

fen = tk.Tk()
fen.title("Enregistrer une Vente")
fen.geometry("500x500")


label_vendeur = tk.Label(fen, text=f"Connecté comme : {vendeur_nom}", font=("Arial", 12, "bold"))
produit_var = tk.StringVar()

produit_var.set(produits[0].nom)

choix_produit = tk.OptionMenu(fen, produit_var, *[ p.nom for p in produits])

choix_produit.pack()

label_quantité = tk.Label(fen, text= "quantité:")
label_quantité.pack()

entre_quantite = tk.Entry(fen)
entre_quantite.pack()

zone = tk.Text(fen, height=10, width=50)
zone.pack()

#fonction bouton 
def ajouter_produit():
    
    quantite = entre_quantite.get()
    produit_choisi = produit_var.get()
    
    if not quantite.isdigit():
        zone.insert(tk.END, "nombre invalide")
        return
    quantite = int(quantite)
    
    produit = next((p for p in produits if p.nom == produit_choisi), None)
    
    if produit:
        
        
        succes = vendeur1.ajouter_article(produit, quantite)
        if succes:
            from stock_manager import sauvegarder_produits
            sauvegarder_produits(produits)
            
            ligne = f"{produit.nom} x {quantite}: {produit.prix * quantite}"
            zone.insert(tk.END, ligne + "\n")

        else: 
            zone.insert(tk.END, f"Stock insuffisant pour {produit.nom} !\n")


def afficher_facture():
    zone.delete("1.0", tk.END)  # On vide d'abord la zone texte
    facture_texte = vendeur1.facture()
    zone.insert(tk.END, facture_texte)
          
            
tk.Button(fen, text = "ajouter à la vente" , command = ajouter_produit).pack()
tk.Button(fen, text="Afficher la facture", command=afficher_facture).pack()




fen.mainloop()
