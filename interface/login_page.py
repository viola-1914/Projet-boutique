# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from auth_manager import verifier_connexion
import subprocess

def lancer_interface(role, username):
    if role == "vendeur":
        subprocess.Popen(["python", "interface/interface_vente.py", username])
    elif role == "admin":
        subprocess.Popen(["python", "interface/interface_vitrine.py"])

def se_connecter():
    username = entry_user.get()
    password = entry_pass.get()

    user = verifier_connexion(username, password)
    if user:
        messagebox.showinfo("Connexion réussie", f"Bienvenue {user.username} ({user.role})")
        fen.destroy()
        lancer_interface(user.role, user.username)
    else:
        messagebox.showerror("Erreur", "Identifiants invalides")

fen = tk.Tk()
fen.title("Connexion")
fen.geometry("300x200")

tk.Label(fen, text="Nom d'utilisateur:").pack()
entry_user = tk.Entry(fen)
entry_user.pack()

tk.Label(fen, text="Mot de passe:").pack()
entry_pass = tk.Entry(fen, show="*")
entry_pass.pack()

tk.Button(fen, text="Se connecter", command=se_connecter).pack(pady=10)

fen.mainloop()
