import tkinter as tk
from googletrans import Translator

def translate_text():
    text = entry.get()
    translator = Translator()
    translation = translator.translate(text, dest='fr')  # Traduction vers l'anglais, vous pouvez changer 'en' par d'autres langues
    translated_label.config(text=translation.text)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Traducteur")

message = tk.Label(root, text="Bienvenue sur mon programme de traduction", fg="green", font=50)
message.pack(pady=50, padx=50)

# Création de l'entrée de texte
texte = tk.Label(root, text="Ecrit ton texte ci-dessous")
texte.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Création du bouton pour traduire
translate_button = tk.Button(root, text="Traduire", command=translate_text, fg="green", font=25)
translate_button.pack(pady=3)

# Création de l'étiquette pour afficher la traduction
translated_label = tk.Label(root, text="", wraplength=400)
translated_label.pack(pady=50, padx=50)

root.mainloop()
