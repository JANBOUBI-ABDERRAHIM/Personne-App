class Personne:
    nb = 0
    
    def __init__(self, nom='', age=''):
        Personne.nb += 1
        self.__cin = Personne.nb
        self.__nom = nom
        self.__age = age
    
    @property
    def getCIN(self):
        return self.__cin
    
    @property
    def getNom(self):
        return self.__nom
    
    @property
    def getAge(self):
        return self.__age
    
    def __str__(self):
        return "Personne :" + str(self.getNom) + " CIN = " + str(self.getCIN) + " Age = " + str(self.getAge)