import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Collision de barres")

# Charger les images des barres
image_barre_gauche = pygame.image.load("Barre.png")
image_barre_droite = pygame.image.load("Barre.png")

# Position initiale des barres
pos_barre_gauche = [50, hauteur // 2 - 25]
pos_barre_droite = [largeur - 70, hauteur // 2 - 25]

# Vitesses de déplacement des barres
vitesse_gauche = 5
vitesse_droite = 5

# Compteur de collisions
compteur_collisions = 0

# Score
score = 0

# Police pour le texte du compteur
font = pygame.font.Font(None, 36)

# Variable pour vérifier si la touche "espace" est enfoncée
espace_appuye = False

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vérification de la collision entre les barres
    collision = pygame.Rect(*pos_barre_gauche, image_barre_gauche.get_width(), image_barre_gauche.get_height()).colliderect(
        pygame.Rect(*pos_barre_droite, image_barre_droite.get_width(), image_barre_droite.get_height()))

    # Si les barres sont à 20 pixels d'écart, augmenter le score lorsque la touche "espace" est enfoncée
    touches = pygame.key.get_pressed()
    if collision or abs(pos_barre_gauche[0] + image_barre_gauche.get_width() - pos_barre_droite[0]) <= 75:
        if touches[pygame.K_SPACE] and not espace_appuye:
            score += 1
            espace_appuye = True
        elif not touches[pygame.K_SPACE]:
            espace_appuye = False
    else:
        # Réinitialiser le jeu si la touche "espace" est enfoncée au mauvais moment
        if touches[pygame.K_SPACE] and not espace_appuye:
            pos_barre_gauche = [50, hauteur // 2 - 25]
            pos_barre_droite = [largeur - 70, hauteur // 2 - 25]
            score = 0
            compteur_collisions = 0
            espace_appuye = True
        elif not touches[pygame.K_SPACE]:
            espace_appuye = False

    # Déplacement des barres
    pos_barre_gauche[0] += vitesse_gauche
    pos_barre_droite[0] -= vitesse_droite

    # Remettre les barres à leur position initiale si elles sont en collision
    if collision:
        compteur_collisions += 1
        pos_barre_gauche = [50, hauteur // 2 - 25]
        pos_barre_droite = [largeur - 70, hauteur // 2 - 25]

    # Effacement de l'écran
    fenetre.fill(BLANC)

    # Dessin des barres
    image_barre_gauche = pygame.transform.scale(image_barre_gauche, (12,64))
    image_barre_droite = pygame.transform.scale(image_barre_droite, (12,64))

    fenetre.blit(image_barre_gauche, pos_barre_gauche)
    fenetre.blit(image_barre_droite, pos_barre_droite)

    # Affichage du compteur de collisions
    texte = font.render(f"Collisions : {compteur_collisions}", True, NOIR)
    fenetre.blit(texte, (10, 10))

    # Affichage du score
    texte_score = font.render(f"Score : {score}", True, NOIR)
    fenetre.blit(texte_score, (largeur - 160, 10))

    # Mise à jour de l'écran
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.delay(9)

# Quitter Pygame
pygame.quit()
sys.exit()