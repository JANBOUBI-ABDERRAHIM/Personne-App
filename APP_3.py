import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Personnes, Formateurs, Stagiaires
import json

with open('./personnes.json', 'r', encoding="utf-8") as fichier:
    personnes = json.load(fichier)

for _ in personnes[:-1]:
    p = Personnes.Personne()

X1, X2, X3 = 20, 160, 330

root = tk.Tk()
root.geometry('1200x650')
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

#################################################
ajouter = tk.Button(text='Création Personne')
ajouter.place(x=X2, y=330)

###################### Search Section ######################
searchLabel = tk.Label(root, text='Rechercher:')
searchLabel.place(x=500, y=20)

searchText = tk.Entry(root, width=25)
searchText.place(x=590, y=20)

filterLabel = tk.Label(root, text='Filtrer par:')
filterLabel.place(x=500, y=50)

filterVar = tk.StringVar()
filterCombo = ttk.Combobox(root, textvariable=filterVar, width=22, state='readonly')
filterCombo['values'] = ('Tous', 'CIN', 'Nom', 'Type', 'Filiere')
filterCombo.current(0)
filterCombo.place(x=590, y=50)

searchBtn = tk.Button(root, text='Rechercher')
searchBtn.place(x=590, y=80)

resetBtn = tk.Button(root, text='Réinitialiser')
resetBtn.place(x=700, y=80)

###################### Table ######################
area = ('CIN', 'Nom', 'Age', 'type', 'Type de contrat', 'Salaire', 'Nbr heures', 'Filiere', 'Note1', 'Note2', 'Moyenne')
ac = ('n', 'e', 's', 'ne', 'nw', 'sw', 'na', 'nb', 'sa', 'nc', 'nd')

tv = ttk.Treeview(root, columns=ac, show='headings', height=7)

for i in range(len(area)):
    widthC = 140
    if area[i] != 'Type de contrat': widthC = 95
    tv.column(ac[i], width=widthC, anchor='e')
    tv.heading(ac[i], text=area[i])

tv.place(x=50, y=370)

# Load initial data
for personne in personnes:
    tv.insert('', 'end', values=tuple(personne.values()))

###################### Delete Button ######################
deleteBtn = tk.Button(root, text='Supprimer la ligne sélectionnée')
deleteBtn.place(x=50, y=570)

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

def delete_row():
    selected_item = tv.selection()
    if not selected_item:
        messagebox.showwarning("Attention", "Veuillez sélectionner une ligne à supprimer")
        return
    
    result = messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cette ligne?")
    if result:
        # Get the CIN of the selected row
        item_values = tv.item(selected_item[0])['values']
        cin_to_delete = str(item_values[0])
        
        # Remove from treeview
        tv.delete(selected_item[0])
        
        # Remove from personnes list
        global personnes
        personnes = [p for p in personnes if str(p['CIN']) != cin_to_delete]
        
        # Save updated list to JSON
        with open('./personnes.json', 'w', encoding="utf-8") as fichier:
            json.dump(personnes, fichier)
        
        messagebox.showinfo("Succès", "Ligne supprimée avec succès")

def search_table():
    search_term = searchText.get().lower()
    filter_by = filterVar.get()
    
    # Clear current table
    for item in tv.get_children():
        tv.delete(item)
    
    # Filter and display results
    for personne in personnes:
        if filter_by == 'Tous':
            # Search in all fields
            if (search_term in str(personne.get('CIN', '')).lower() or
                search_term in str(personne.get('nom', '')).lower() or
                search_term in str(personne.get('type', '')).lower() or
                search_term in str(personne.get('filier', '')).lower()):
                tv.insert('', 'end', values=tuple(personne.values()))
        elif filter_by == 'CIN':
            if search_term in str(personne.get('CIN', '')).lower():
                tv.insert('', 'end', values=tuple(personne.values()))
        elif filter_by == 'Nom':
            if search_term in str(personne.get('nom', '')).lower():
                tv.insert('', 'end', values=tuple(personne.values()))
        elif filter_by == 'Type':
            if search_term in str(personne.get('type', '')).lower():
                tv.insert('', 'end', values=tuple(personne.values()))
        elif filter_by == 'Filiere':
            if search_term in str(personne.get('filier', '')).lower():
                tv.insert('', 'end', values=tuple(personne.values()))

def reset_search():
    searchText.delete(0, 'end')
    filterCombo.current(0)
    
    # Clear and reload all data
    for item in tv.get_children():
        tv.delete(item)
    
    for personne in personnes:
        tv.insert('', 'end', values=tuple(personne.values()))

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

# Bind real-time search (optional - searches as you type)
def on_search_key(event):
    if searchText.get():
        search_table()
    else:
        reset_search()

searchText.bind('<KeyRelease>', on_search_key)

ajouter.config(command=add)
deleteBtn.config(command=delete_row)
searchBtn.config(command=search_table)
resetBtn.config(command=reset_search)

case1.bind("<Button-1>", modifVisib)
case1.focus_set()
case2.bind('<Button-1>', modifVisib)
case2.focus_set()

root.mainloop()