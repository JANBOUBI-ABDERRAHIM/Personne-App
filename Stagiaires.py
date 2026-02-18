from Personnes import Personne

class Stagiaire(Personne):
    def __init__(self, nom, age, filier, note1, note2):
        super().__init__(nom, age)
        self.filier=filier
        self.note1=note1
        self.note2=note2
        self.moyenne = (self.note1 + self.note2) / 2
        print(f"Personne.nb: {Personne.nb}")
    
    @property
    def getFilier(self):
        return self.filier
    @property
    def getMoyenne(self):
        return self.moyenne
    
    def __str__(self):
        return Personne.__str__(self) + " filier: " + self.filier + " moyenne des notes: " + self.moyenne