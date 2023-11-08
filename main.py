from Niveau import Niveau
from Jeu import Jeu

def main():
    print("Récupération des données")

    Levelfile1="test2.py"
    Levelfile2="test2.py"
    Levelfile3="test2.py"

    with open("data.txt") as file:
        contenue=file.read()

    if contenue=="3" or contenue=="F":
        n1=Niveau(1,Levelfile1,True)
        n2=Niveau(2,Levelfile2,True)
        n3=Niveau(3,Levelfile3,True)
    elif contenue=="2":
        n1=Niveau(1,Levelfile1,True)
        n2=Niveau(2,Levelfile2,True)
        n3=Niveau(3,Levelfile3,False)    
    else:
        f = open("data.txt","w")
        f.write("1")
        f.close()
        n1=Niveau(1,Levelfile1,True)
        n2=Niveau(2,Levelfile2,False)
        n3=Niveau(3,Levelfile3,False)

    niveaux=[n1,n2,n3]
    game=Jeu(niveaux)
    if contenue=="F":
        game.setTrueEstFini()
    game.interface()

main()

