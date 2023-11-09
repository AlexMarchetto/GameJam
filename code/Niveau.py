class Niveau:
    def __init__(self,num,nomFichier,estValider) -> None:
        self.num=num
        self.nomFichier=nomFichier
        self.estValider=estValider

    def getNum(self):
        return self.num
    
    def getNomFichier(self):
        return self.nomFichier
    
    def getEstValider(self):
        return self.estValider
    
    def niveauInterface(self):
        print("Création de l'interface du niveau")