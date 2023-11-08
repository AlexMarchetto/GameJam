import pygame
import sys
from Book import Book

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))

# Titre de la fenêtre
pygame.display.set_caption("Interface Pygame Simple")

c1=Book(ecran,100,100,"book2.png")
c1.setTrueIsFounded()

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Logique de jeu et dessin ici

    c1.draw()

    # Actualiser l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
