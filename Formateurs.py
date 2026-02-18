from Personnes import Personne

class Formateur(Personne):
    def __init__(self, nom, age, type_contrat, salaire, nbr_heures):
        super().__init__(nom, age)
        self.type_contrat=type_contrat
        self.salaire=salaire
        self.nbr_heures=nbr_heures
        print(f"Personne.nb: {Personne.nb}")
    
    @property
    def getTypeContrat(self):
        return self.type_contrat
    @property
    def getSalaire(self):
        return self.salaire
    @property
    def getNbrHeures(self):
        return self.nbr_heures
    
    def __str__(self):
        return Personne.__str__(self) + " type contrat: " + self.type_contrat + " salaire: " + self.salaire + " nbr heures: " + self.nbr_heures