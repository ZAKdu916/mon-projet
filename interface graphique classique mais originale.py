import tkinter as tk
from tkinter import ttk

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Interface Graphique Classique mais Originale")
root.geometry("800x600")
root.config(bg="#2C3E50")

# Style personnalisé
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12), foreground="#ECF0F1", background="#2980B9")
style.configure("TLabel", font=("Helvetica", 14), foreground="#ECF0F1", background="#2C3E50")

# Titre
title_label = ttk.Label(root, text="Bienvenue sur l'interface graphique!", style="TLabel")
title_label.pack(pady=20)

# Champ de saisie
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Helvetica", 12), width=40)
entry.pack(pady=10)

# Bouton d'action
def on_button_click():
    user_text = entry_var.get()
    result_label.config(text=f"Vous avez saisi : {user_text}")

button = ttk.Button(root, text="Valider", command=on_button_click, style="TButton")
button.pack(pady=10)

# Label de résultat
result_label = ttk.Label(root, text="", style="TLabel")
result_label.pack(pady=20)

# Démarrage de la boucle principale
root.mainloop()