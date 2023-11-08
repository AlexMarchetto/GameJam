import pygame
import os
import sys
import time
from Niveau import Niveau
class Jeu:
    def __init__(self,niveaux):
        self.niveaux=niveaux
        self.estFini=False

    def setTrueEstFini(self):
        self.estFini=True

    def interface(self):
        print("Création de l'interface principale")

        # Initialisation de Pygame
        pygame.init()

        # Paramètres de la fenêtre
        largeur_fenetre = 800
        hauteur_fenetre = 600
        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
        pygame.display.set_caption("Sélection de Niveau")

        # Charger une image en tant que fond d'écran
        fond = pygame.image.load("leo.jpg")
        fond = pygame.transform.scale(fond, (largeur_fenetre, hauteur_fenetre))

        # Couleurs
        blanc = (255, 255, 255)
        noir = (0, 0, 0)
        rouge = (255, 0, 0)
        gris = (150, 150, 150)  # Nouvelle couleur pour les niveaux non terminés

        # Polices de texte
        police = pygame.font.Font(None, 36)

        # Phrase en haut de l'interface
        if not(self.estFini):
            phrase = "Sélectionnez un niveau"
        else:
            phrase = "Vous avez terminé tous les niveaux"
        phrase_texte = police.render(phrase, True, noir)
        phrase_x = largeur_fenetre // 2 - phrase_texte.get_width() // 2
        phrase_y = 20

        # Bouton "Réinitialiser"
        bouton_reinitialiser = pygame.Rect(10, hauteur_fenetre - 60, 90, 40)
        couleur_bouton = gris
        couleur_bouton_active = rouge
        bouton_texte = police.render("Reset", True, noir)

        # Niveaux et leur état de terminaison
        nomNiveaux=[]
        niveaux_termines = []
        for niveau in self.niveaux:
            nomNiveaux.append("Niveau "+str(niveau.getNum()))
            niveaux_termines.append(niveau.getEstValider())

        #btn image
        img1=pygame.image.load("img1.png")
        img2OK=pygame.image.load("img1.png")
        img2KO=pygame.image.load("img1.png")
        img3OK=pygame.image.load("img1.png")
        img3KO=pygame.image.load("img1.png")

        img1 = pygame.transform.scale(img1,(200,200))
        img2OK = pygame.transform.scale(img2OK,(200,200))
        img2KO = pygame.transform.scale(img2KO,(200,200))
        img3OK = pygame.transform.scale(img3OK,(200,200))
        img3KO = pygame.transform.scale(img3KO,(200,200))
    
        niveau_selectionne=""

        # Boucle principale
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_reinitialiser.collidepoint(event.pos):
                        print("Bouton Réinitialiser cliqué")
                        niveau_selectionne="init"
                        en_cours = False
                    # Vérifier si un niveau a été sélectionné
                    for i, (niveau, termine) in enumerate(zip(nomNiveaux, niveaux_termines)):
                        rect=img1.get_rect()
                        x = largeur_fenetre // 3 +40
                        y = 150 + i * 110
                        rect.topleft = (x,y)
                        if rect.collidepoint(event.pos):
                            if termine:
                                niveau_selectionne=niveau
                                en_cours=False

            fenetre.fill(blanc)
            # Afficher le fond d'écran
            fenetre.blit(fond, (0, 0))

            # Afficher la phrase en haut de l'interface
            fenetre.blit(phrase_texte, (phrase_x, phrase_y))

             # Dessiner le bouton "Réinitialiser"
            pygame.draw.rect(fenetre, couleur_bouton, bouton_reinitialiser)
            fenetre.blit(bouton_texte, (bouton_reinitialiser.x + 10, bouton_reinitialiser.y + 10))

            for i, (niveau, termine) in enumerate(zip(nomNiveaux, niveaux_termines)):
                x = largeur_fenetre // 3 +40
                y = 150 + i * 110
                if termine:
                    if niveau=="Niveau 1":
                        fenetre.blit(img1,(x,y))
                    elif niveau=="Niveau 2":
                        fenetre.blit(img2OK,(x,y))
                    else:
                        fenetre.blit(img3OK,(x,y))
                else:
                    if niveau=="Niveau 2":
                        fenetre.blit(img2KO,(x,y))
                    else:
                        fenetre.blit(img3KO,(x,y))

            pygame.display.flip()

        pygame.quit()

        time.sleep(0.2)

        # Exécute le code du niveau correspondant
        if niveau_selectionne == "Niveau 1":
            print("Exécute Niveau 1")
            os.system("python "+self.niveaux[0].getNomFichier())
        elif niveau_selectionne == "Niveau 2":
            print("Exécute Niveau 2")
            os.system("python "+self.niveaux[1].getNomFichier())
        elif niveau_selectionne == "Niveau 3":
            print("Exécute Niveau 3")
            os.system("python "+self.niveaux[2].getNomFichier())
        elif niveau_selectionne == "init":
            print("Réini")
            f = open("data.txt","w")
            f.write("1")
            f.close()
            time.sleep(1)
            os.system("python main.py")
        sys.exit()