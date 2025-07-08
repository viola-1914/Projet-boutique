import tkinter as tk
#from data import produits

fen = tk.Tk()
fen.title("Boutique - Vitrine des Produits")
fen.geometry("500x400")

entete_font = ("Arial", 12, "bold")
contenu_font = ("Arial", 11)

# ➜ Créer une frame pour le tableau
tableau_frame = tk.Frame(fen)
tableau_frame.pack(padx=10, pady=10)

# ➜ Fonction qui dessine le tableau
def afficher_tableau():
    
    from stock_manager import charger_produits
    global produits
    produits = charger_produits()
    # Effacer ce qui était dedans
    for widget in tableau_frame.winfo_children():
        widget.destroy()
    
    # Entêtes
    entetes = ["Produit", "Prix Unitaire", "Stock Disponible", "Stock Limite"]
    for col, texte in enumerate(entetes):
        label = tk.Label(tableau_frame, text=texte, font=entete_font, borderwidth=2, relief="groove", padx=10, pady=5)
        label.grid(row=0, column=col, sticky="nsew")
    
    # Lignes des produits
    for i, p in enumerate(produits, start=1):
        ligne = [
            p.nom,
            f"{p.prix} FCFA",
            p.stock_disponible,
            p.stock_limite
        ]
        for col, valeur in enumerate(ligne):
            label = tk.Label(tableau_frame, text=valeur, font=contenu_font, borderwidth=1, relief="solid", padx=10, pady=5)
            label.grid(row=i, column=col, sticky="nsew")

    # Rendre les colonnes élastiques
    for col in range(len(entetes)):
        tableau_frame.grid_columnconfigure(col, weight=1)

# ➜ Afficher la première fois au lancement
afficher_tableau()

# ➜ Bouton pour rafraîchir
btn_maj = tk.Button(fen, text="Mettre à jour", command=afficher_tableau)
btn_maj.pack(pady=20)

fen.mainloop()
