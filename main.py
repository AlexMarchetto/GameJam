from Niveau import Niveau
from Jeu import Jeu

def main():
    print("Récupération des données")

    with open("data.txt") as file:
        contenue=file.read()

    if contenue=="3" or contenue=="F":
        n1=Niveau(1,"niveau1.py",True)
        n2=Niveau(2,"niveau2.py",True)
        n3=Niveau(3,"niveau3.py",True)
    elif contenue=="2":
        n1=Niveau(1,"test2.py",True)
        n2=Niveau(2,"niveau2.py",True)
        n3=Niveau(3,"niveau3.py",False)    
    else:
        f = open("data.txt","w")
        f.write("1")
        f.close()
        n1=Niveau(1,"test2.py",True)
        n2=Niveau(2,"niveau2.py",False)
        n3=Niveau(3,"niveau3.py",False)

    niveaux=[n1,n2,n3]
    game=Jeu(niveaux)
    if contenue=="F":
        game.setTrueEstFini()
    game.interface()

main()

