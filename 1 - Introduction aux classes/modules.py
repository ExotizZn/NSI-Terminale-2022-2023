""" ********************************************************************
* Fichier de module du groupe NSI terminale Dumont d'Urville 2022-2023 * 
******************************************************************** """

class humain :
    # attributs
    def __init__(self, size, weight, birth, sex, surname, forname):
        self.taille   = size
        self.masse    = weight
        self.dateNais = birth
        self.sexe     = sex
        self.nom      = surname
        self.prenom   = forname
        self.corrige()
    
    # methodes
    def age(self):
        return 'pas fini'
    
    def thai(self, val=None):
        return 'pas fini'
    
    def regime(self, val):
        self.masse = self.mass + val
    
    def secateur(self, val):
        self.taille -= val 

    def corrige(self):
        self.nom=self.nom.lower()
        self.nom=self.nom[0].upper()+self.nom[1:]
        self.prenom= self.prenom.lower()
        self.prenom=self.prenom[0].upper()+self.prenom[1:]
    
    
    
    
    
    
    
    
    
