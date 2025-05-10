import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

login = ctk.CTk()
login.title("ctk")
login.geometry("500x350")

def connexion():
    print("Bienvenue")

frame = ctk.CTkFrame(master=login)
frame.pack(pady=20, padx=60, fill="both", expand=True)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="Identifiant")
champ1.pack(pady=12)

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
champ2.pack(pady=12)

bouton = ctk.CTkButton(master=frame, text="Connexion", command=connexion)
bouton.pack(pady=12, padx=10)

label = ctk.CTkLabel(master=frame, text="")
label.pack(pady=12, padx=10)





login.mainloop()
