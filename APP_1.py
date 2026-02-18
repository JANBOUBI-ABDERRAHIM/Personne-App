import tkinter as tk
from tkinter import ttk
import Personnes, Formateurs, Stagiaires
import json

with open('./personnes.json', 'r', encoding="utf-8") as fichier:
    personnes = json.load(fichier)

for _ in personnes[:-1]:
    b =  Personnes.Personne()

X1, X2, X3 = 20, 160, 330

root = tk.Tk()
root.geometry('1200x600')
root.title('Gestion des Personnes')

cinDefaultValue = str(Personnes.Personne().nb+1) if len(personnes)>0 else '1'

cinLabel = tk.Label(root, text='CIN:')  
cinLabel1 = tk.Label(root, text=cinDefaultValue)
cinLabel1.config(state=tk.DISABLED)
cinLabel.place(x=X1, y=20)
cinLabel1.place(x=X2, y=20)

nomLabel = tk.Label(root, text='Nom:')  
nomText = tk.Entry(root)  
nomLabel.place(x=X1, y=50)
nomText.place(x=X2, y=50)

ageLabel = tk.Label(root, text='Age:')  
ageText = tk.Entry(root)  
ansLabel = tk.Label(root, text='ans')  
ageLabel.place(x=X1, y=80)
ageText.place(x=X2, y=80)
ansLabel.place(x=X3, y=80)

TypeLabel = tk.Label(root, text='Type:')  

v = tk.IntVar()
case1 = tk.Radiobutton(root, variable=v, value=1)  
case2 = tk.Radiobutton(root, variable=v, value=2)  
case1.config(text='Formateur')
case2.config(text='Stagiare')
v.set(1)  
TypeLabel.place(x=X1, y=110)
case1.place(x=X2, y=110)
case2.place(x=X3, y=110)
case1.config(state=tk.NORMAL)

###################### Formateure ######################
# Type de Contrat
typeContratLabel = tk.Label(root, text='Type de Contrat: ')  
typeContratText = tk.Entry(root)  
typeContratLabel.place(x=X1, y=140)
typeContratText.place(x=X2, y=140)
# Salaire
salaireLabel = tk.Label(root, text='Salaire: ')  
salaireText = tk.Entry(root)  
salaireEuroLabel = tk.Label(root, text='euro')  
salaireLabel.place(x=X1, y=170)
salaireText.place(x=X2, y=170)
salaireEuroLabel.place(x=X3, y=170)
# Nombre d'heures
nbHeuresLabel = tk.Label(root, text='Nombre des heures: ')  
nbHeuresText = tk.Entry(root)  
nbHeuresEuroLabel = tk.Label(root, text='heure')  
nbHeuresLabel.place(x=X1, y=200)
nbHeuresText.place(x=X2, y=200)
nbHeuresEuroLabel.place(x=X3, y=200)

###################### Stagiaire ######################
# Filier
filierLabel = tk.Label(root, text='Filier: ')  
filierText = tk.Entry(root)  
filierLabel.place(x=X1, y=240)
filierText.place(x=X2, y=240)
filierText.config(state=tk.DISABLED)
# Note 1
Note1Label = tk.Label(root, text='Note 1: ')  
Note1Text = tk.Entry(root)  
Note1EuroLabel = tk.Label(root, text='/ 20')  
Note1Label.place(x=X1, y=270)
Note1Text.place(x=X2, y=270)
Note1EuroLabel.place(x=X3, y=270)
Note1Text.config(state=tk.DISABLED)
# Note 2
Note2Label = tk.Label(root, text='Note 2: ')  
Note2Text = tk.Entry(root)  
Note2EuroLabel = tk.Label(root, text='/ 20')  
Note2Label.place(x=X1, y=300)
Note2Text.place(x=X2, y=300)
Note2EuroLabel.place(x=X3, y=300)
Note2Text.config(state=tk.DISABLED)
#################################################33
ajouter = tk.Button(text='Création Personne')
ajouter.place(x=X2, y=330)

area = ('CIN', 'Nom', 'Age', 'type', 'Type de contrat', 'Salaire', 'Nbr heures', 'Filiere', 'Note1', 'Note2', 'Moyenne')
ac = ('n', 'e', 's', 'ne', 'nw', 'sw', 'na', 'nb', 'sa', 'nc', 'nd')

tv = ttk.Treeview(root, columns=ac, show='headings', height=7)

for i in range(len(area)):
    widthC = 140
    if area[i] != 'Type de contrat': widthC = 95
    tv.column(ac[i], width=widthC, anchor='e')
    tv.heading(ac[i], text=area[i])

tv.place(x=50, y=370)

for personne in personnes:
    tv.insert('', 'end', values=tuple(personne.values()))

####################################################
o = ""

def add():
    print(str(v.get()))
    if(str(v.get()) =='1'):
        o = 'Formateur'
        c = Formateurs.Formateur(nomText.get(), ageText.get(), typeContratText.get(), salaireText.get(), nbHeuresText.get())
        cc = (str(c.getCIN), nomText.get(), ageText.get(), 'Formateur', typeContratText.get(), salaireText.get(), nbHeuresText.get(), '', '', '', '')
    else:
        o = 'Stagiaire'
        c = Stagiaires.Stagiaire(nomText.get(), ageText.get(), filierText.get(), float(Note1Text.get()), float(Note2Text.get()))
        cc = (str(c.getCIN), nomText.get(), ageText.get(), 'Stagiaire', '', '', '', filierText.get(), Note1Text.get(), Note2Text.get(), str(c.getMoyenne))
    
    cinLabel1.config(text=str(Personnes.Personne.nb + 1))
    tv.insert('', 'end', values=cc)
    personnes.append({
        'CIN': cc[0],
        'nom': cc[1],
        'age': cc[2],
        'type': cc[3],
        'typeContrat': cc[4],
        'salaire': cc[5],
        'nbHeures': cc[6],
        'filier': cc[7],
        'note1': cc[8],
        'note2': cc[9],
        'moyenne': cc[10],
    })

    # save the new line into a json file
    with open('./personnes.json', 'w', encoding="utf-8") as fichier:
        json.dump(personnes, fichier)

    nomText.delete(0, 'end')
    ageText.delete(0, 'end')
    
    typeContratText.delete(0, 'end')
    salaireText.delete(0, 'end')
    nbHeuresText.delete(0, 'end')
    
    filierText.delete(0, 'end')
    Note1Text.delete(0, 'end')
    Note2Text.delete(0, 'end')

def modifVisib(evt):
    print(str(v.get()))
    if(str(v.get()) == '2'):
        typeContratText.config(state=tk.NORMAL)
        salaireText.config(state=tk.NORMAL)
        nbHeuresText.config(state=tk.NORMAL)
        filierText.config(state=tk.DISABLED)
        Note1Text.config(state=tk.DISABLED)
        Note2Text.config(state=tk.DISABLED)
    if(str(v.get()) == '1'):
        typeContratText.config(state=tk.DISABLED)
        salaireText.config(state=tk.DISABLED)
        nbHeuresText.config(state=tk.DISABLED)
        filierText.config(state=tk.NORMAL)
        Note1Text.config(state=tk.NORMAL)
        Note2Text.config(state=tk.NORMAL)

ajouter.config(command=add)
case1.bind("<Button-1>", modifVisib)
case1.focus_set()
case2.bind('<Button-1>', modifVisib)
case2.focus_set()

root.mainloop()