import pygame
import sys
import os
import time

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Sélection de Niveau")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
gris = (150, 150, 150)  # Nouvelle couleur pour les niveaux non terminés

# Polices de texte
police = pygame.font.Font(None, 36)

# Niveaux et leur état de terminaison
niveaux = ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4"]
niveaux_termines = [True, False, False, False]  # Exemple, indiquez l'état de chaque niveau

# Fonction pour afficher le texte et les niveaux
def afficher_niveaux():
    fenetre.fill(blanc)
    for i, (niveau, termine) in enumerate(zip(niveaux, niveaux_termines)):
        if termine:
            couleur_texte = noir
        else:
            couleur_texte = gris

        texte = police.render(niveau, True, couleur_texte)
        x = largeur_fenetre // 2 - texte.get_width() // 2
        y = 100 + i * 100
        fenetre.blit(texte, (x, y))
        if termine:
            pygame.draw.rect(fenetre, rouge, (x - 10, y - 10, texte.get_width() + 20, texte.get_height() + 20), 2)

niveau_selectionne=""

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si un niveau a été sélectionné
            for i, (niveau, termine) in enumerate(zip(niveaux, niveaux_termines)):
                if termine:
                    x = largeur_fenetre // 2 - police.size(niveau)[0] // 2
                    y = 100 + i * 100
                    if x - 10 < event.pos[0] < x + police.size(niveau)[0] + 10 and y - 10 < event.pos[1] < y + police.size(niveau)[1] + 10:
                        niveau_selectionne = niveau
                        print("Niveau sélectionné:", niveau_selectionne)
                        en_cours = False

    afficher_niveaux()
    pygame.display.flip()

pygame.quit()

time.sleep(0.2)

# Exécute le code du niveau correspondant
if niveau_selectionne == "Niveau 1":
    print("Exécute Niveau 1")
    os.system("python test2.py")
elif niveau_selectionne == "Niveau 2":
    print("Exécute Niveau 2")
    os.system("python niveau2.py")
elif niveau_selectionne == "Niveau 3":
    print("Exécute Niveau 3")
    os.system("python niveau3.py")
sys.exit()


