import tkinter as tk
import subprocess

fen = tk.Tk()
fen.title("Page d'Accueil - Gestion Boutique")
fen.geometry("400x300")
fen.configure(bg="#f0f0f0")

titre = tk.Label(fen, text="Bienvenue dans la Boutique", font=("Arial", 16, "bold"), bg="#f0f0f0")
titre.pack(pady=20)

# ➜ Boutons jolis
btn_style = {"font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5}

def ouvrir_vitrine():
    subprocess.Popen(["python", "interface/interface_vitrine.py"])

def ouvrir_vente():
    # Ici on pourrait aussi lancer interface_login si tu veux obliger à se connecter avant
    subprocess.Popen(["python", "interface/interface_login.py"])

def ouvrir_login():
    subprocess.Popen(["python", "interface/interface_login.py"])

tk.Button(fen, text="Voir la Vitrine des Produits", command=ouvrir_vitrine, **btn_style).pack(pady=10)
tk.Button(fen, text="Enregistrer une Vente", command=ouvrir_vente, **btn_style).pack(pady=10)
tk.Button(fen, text="Connexion Utilisateur", command=ouvrir_login, **btn_style).pack(pady=10)

fen.mainloop()

