import tkinter as tk
import subprocess
import os

def ouvrir_vitrine():
    chemin = os.path.join("interface", "interface_vitrine.py")
    subprocess.Popen(["python", chemin])

fen = tk.Tk()
fen.title("Accueil")
fen.geometry("300x200")

btn = tk.Button(fen, text="Ouvrir Vitrine", command=ouvrir_vitrine)
btn.pack(pady=20)

fen.mainloop()
