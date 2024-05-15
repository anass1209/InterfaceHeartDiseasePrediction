import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date
import joblib
from PIL import Image, ImageTk

# Charger le modèle pré-entraîné
model = joblib.load('heart_Disease_model.pkl')

def analysis():
    # Obtenir les données saisies par l'utilisateur
    name = Name.get()
    A = today.year - DOB.get()
    try:
        B = selection()
        F = selection2()
        I = selection3()
        C = int(selection4())
        G = int(restecg_combobox.get())
        K = int(selection5())
        L = int(ca_combobox.get())
        M = int(thal_combobox.get())
        D = int(trestbps.get())
        E = int(chol.get())
        H = int(thalach.get())
        J = int(oldpeak.get())
        N =  int(age.get())
    except ValueError as e:
        messagebox.showerror("Missing", "Please fill all fields correctly!")
        return

    # Prétraiter les données saisies par l'utilisateur
    user_data = [[A, B, C, D, E, F, G, H, I, J, K, L, M]]
    user_data_int = [[int(value) for value in sublist] for sublist in user_data]

    # Effectuer des prédictions
    prediction = model.predict(user_data_int)

    # Afficher le résultat
    if prediction == 1:
        result_image = ImageTk.PhotoImage(Image.open("Images/heart_disease.png"))
    else:
        result_image = ImageTk.PhotoImage(Image.open("Images/no_heart_disease.png"))

    # Afficher le rapport dans la zone spécifiée
    result_image_label.config(image=result_image)
    result_image_label.image = result_image
    result_image_label.place(x=590, y=450, width=726, height=264)

def logout():
    root.destroy()

def clear_fields():
    Name.set("")
    DOB.set(0)
    gen.set(0)
    fbs.set(0)
    exang.set(0)
    cp_combobox.set("")
    restecg_combobox.set("")
    slope_combobox.set("")
    ca_combobox.set("")
    thal_combobox.set("")
    trestbps.set("")
    chol.set("")
    thalach.set("")
    oldpeak.set("")
    age.set("")


def selection():
    if gen.get() == 1:
        Gender = 1
        return Gender
    elif gen.get() == 2:
        Gender = 0
        return Gender
    else:
        raise ValueError("Gender not selected")

def selection2():
    if fbs.get() == 1:
        Fbs = 1
        return (Fbs)
    elif fbs.get() == 2:
        Fbs = 0
        return (Fbs)
    else:
        raise ValueError("Fbs not selected")

def selection3():
    if exang.get() == 1:
        Exang = 1
        return (Exang)

    elif exang.get() == 2:
        Exang = 0
        return (Exang)
    else:
        raise ValueError("Exang not selected")

def selection4():
    input = cp_combobox.get()
    if input == "0 = typical angina":
        return (0)
    elif input == "1 = atypical angina":
        return (1)
    elif input == "2 = non-anginal pain":
        return (2)
    elif input == "3 = asymptomatic":
        return (3)
    else:
        raise ValueError("cp not selected")

def selection5():
    input = slope_combobox.get()
    if input == "0 = upsloping":
        return (0)
    elif input == "1 = flat":
        return (1)
    elif input == "2 = downsloping":
        return (2)
    else:
        raise ValueError("slop not selected")

def show_coordinates(event):
    x = event.x
    y = event.y
    coordinate_label.config(text=f"x={x}, y={y}")

# Initialiser la fenêtre principale
root = tk.Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False, False)

# Définir les couleurs de fond et de cadre
background = "#FFFFFF"
framebg = "#62a7ff"
framefg = "#fefbfb"
colore_top ="#EFEFEF"
# Définition de l'icône de la fenêtre
image_icon = tk.PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# Section d'en-tête
# Charger et placer l'image d'en-tête
logo = tk.PhotoImage(file="Images/header.png")
myimage = tk.Label(image=logo, bg=background)
myimage.place(x=0, y=0)

# Cadre pour les informations du patient
Heading_entry = tk.Frame(root, width=800, height=190, bg="#57A4FF")
Heading_entry.place(x=600, y=20)

# Labels pour les champs de saisie
tk.Label(Heading_entry, text="Registration No", font="arial 13", bg="#57A4FF", fg=framefg).place(x=30, y=0)
tk.Label(Heading_entry, text="Date", font="arial 13", bg="#57A4FF", fg=framefg).place(x=430, y=0)
tk.Label(Heading_entry, text="Patient Name", font="arial 13",bg="#57A4FF",fg=framefg).place(x=30, y=90)
tk.Label(Heading_entry, text="Birth Year", font="arial 13",bg="#57A4FF", fg=framefg).place(x=430, y=90)

# Chargement des images pour les champs de saisie
Entry_image = tk.PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_image2 = tk.PhotoImage(file="Images/Rounded Rectangle 1.png")

# Placement des images de champ de saisie
tk.Label(Heading_entry, image=Entry_image).place(x=28, y=30)
tk.Label(Heading_entry, image=Entry_image).place(x=430, y=30)
tk.Label(Heading_entry, image=Entry_image2).place(x=28, y=120)
tk.Label(Heading_entry, image=Entry_image2).place(x=430, y=120)

# Variables pour stocker les informations du patient
Registration = tk.IntVar()
Date = tk.StringVar()
Name = tk.StringVar()
DOB = tk.IntVar()


# Champs de saisie pour les informations du patient
reg_entry = tk.Entry(Heading_entry, textvariable=Registration, width=20, font="arial 15", bg=framefg, bd=0, justify='left')
reg_entry.place(x=30 + 1, y=45)

today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = tk.Entry(Heading_entry, textvariable=Date, width=20, font='arial 15', bg=framefg, bd=0, justify='left')
date_entry.place(x=500 + 1, y=45)
Date.set(d1)

name_entry = tk.Entry(Heading_entry, textvariable=Name, width=20, font="arial 15", bg=framefg, bd=0, justify='left')
name_entry.place(x=30 + 1, y=130)

dob_entry = tk.Entry(Heading_entry, textvariable=DOB, width=20, font="arial 15", bg=framefg, bd=0, justify='left')
dob_entry.place(x=450 + 1, y=130)
# ---------------------------------------------------Corps de l'application----------------------------------------------------------------
# Cadre pour les détails médicaux
Detail_entry = tk.Frame(root, width=490, height=260, bg="#dbe0e3")
Detail_entry.place(x=30, y=450)

# Labels pour les différents champs médicaux
tk.Label(Detail_entry, text="sex:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=10)
tk.Label(Detail_entry, text="fbs: ", font="arial 13", bg=framebg, fg=framefg).place(x=180, y=10)
tk.Label(Detail_entry, text="exang: ", font="arial 13", bg=framebg, fg=framefg).place(x=335, y=10)

# Variables pour les radiobuttons
gen = tk.IntVar()
fbs = tk.IntVar()
exang = tk.IntVar()

# Fonctions pour capturer la sélection des radiobuttons

# Création des radiobuttons pour le sexe, fbs et exang
R1 = tk.Radiobutton(Detail_entry, text='Male', variable=gen, value=1)
R2 = tk.Radiobutton(Detail_entry, text="Female", variable=gen, value=2)
R3 = tk.Radiobutton(Detail_entry, text='True', variable=fbs, value=1)
R4 = tk.Radiobutton(Detail_entry, text="False", variable=fbs, value=2)
R5 = tk.Radiobutton(Detail_entry, text='Yes', variable=exang, value=1)
R6 = tk.Radiobutton(Detail_entry, text="No", variable=exang, value=2)

# Placement des radiobuttons
R1.place(x=43, y=10)
R2.place(x=93, y=10)
R3.place(x=213, y=10)
R4.place(x=263, y=10)
R5.place(x=387, y=10)
R6.place(x=430, y=10)

# Labels pour les autres champs médicaux
tk.Label(Detail_entry, text="cp:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=50)
tk.Label(Detail_entry, text="restecg:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=90)
tk.Label(Detail_entry, text="slope:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=130)
tk.Label(Detail_entry, text="ca:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=170)
tk.Label(Detail_entry, text="thal:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=210)

# Combobox pour les différents champs médicaux avec options prédéfinies
cp_combobox = ttk.Combobox(Detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-anginal pain', '3 = asymptomatic'], font="arial 12", state="r", width=11)
restecg_combobox = ttk.Combobox(Detail_entry, values=['0', '1', '2'], font="arial 12", state="r", width=11)
slope_combobox = ttk.Combobox(Detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font="arial 12", state="r", width=11)
ca_combobox = ttk.Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font="arial 12", state="r", width=11)
thal_combobox = ttk.Combobox(Detail_entry, values=['0', '1', '2', '3'], font="arial 12", state="r", width=11)

# Placement des combobox
cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=80, y=90)
slope_combobox.place(x=70, y=130)
ca_combobox.place(x=50, y=170)
thal_combobox.place(x=50, y=210)

# Labels pour les champs de saisie numériques
tk.Label(Detail_entry, text="trestbps:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=239, y=50)
tk.Label(Detail_entry, text="chol:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=90)
tk.Label(Detail_entry, text="thalach:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=130)
tk.Label(Detail_entry, text="oldpeak:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=170)
tk.Label(Detail_entry, text="age:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=209)

# Variables pour stocker les informations numériques
trestbps = tk.StringVar()
chol = tk.StringVar()
thalach = tk.StringVar()
oldpeak = tk.StringVar()
age = tk.StringVar()

# Champs de saisie pour les informations numériques
trestbps_entry = tk.Entry(Detail_entry, textvariable=trestbps, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
chol_entry = tk.Entry(Detail_entry, textvariable=chol, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
thalach_entry = tk.Entry(Detail_entry, textvariable=thalach, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
oldpeak_entry = tk.Entry(Detail_entry, textvariable=oldpeak, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
age_entry = tk.Entry(Detail_entry, textvariable=age, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)

# Placement des champs de saisie numériques
trestbps_entry.place(x=320, y=50)
chol_entry.place(x=320, y=90)
thalach_entry.place(x=320, y=130)
oldpeak_entry.place(x=320, y=170)
age_entry.place(x=320, y=210)

# ---------------------------------------------------Section de Result----------------------------------------------------------------

# Chargement de l'image de fond du rapport
result_image_label = tk.Label(root, bg=background)
result_image_label.place(x=600, y=270, width=1, height=150)

# Label pour afficher les coordonnées du curseur
coordinate_label = tk.Label(root, text="", bg=background, font="arial 12")
coordinate_label.place(x=0, y=0)

# Bind l'événement <Motion> à la fonction show_coordinates
root.bind("<Motion>", show_coordinates)

# Label pour afficher le développeur
developer_label = tk.Label(root, text="Développé par Anass El-achham", bg=background, font="arial 12")
developer_label.place(x=1212, y=708)
# ---------------------------------------------------Boutons et options----------------------------------------------------------------

# Chargement des images pour les boutons
analysis_button = tk.PhotoImage(file="Images/Analysis.png")
clear_button = tk.PhotoImage(file="Images/clear.png")
info_button = tk.PhotoImage(file="Images/info.png")

# Création des boutons
tk.Button(root, image=analysis_button, bd=0, bg=background, cursor='hand2', command=analysis).place(x=1068, y=278)
tk.Button(root, image=info_button, bd=0, bg=background, cursor='hand2').place(x=1332, y=291)
tk.Button(root, image=clear_button, bd=0, bg=background, cursor='hand2',command=clear_fields).place(x=1212, y=291)

# Bouton pour se déconnecter
logout_icon = tk.PhotoImage(file="Images/logout.png")
logout_button = tk.Button(root, image=logout_icon, bg="#df2d4b", cursor='hand2', bd=0, command=logout)
logout_button.place(x=1390, y=60)

# Démarrage de la boucle principale de l'interface graphique
root.mainloop()
