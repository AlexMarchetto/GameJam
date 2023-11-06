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

# Barres
barre_gauche = pygame.Rect(50, hauteur // 2 - 25, 20, 50)
barre_droite = pygame.Rect(largeur - 70, hauteur // 2 - 25, 20, 50)

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
    collision = barre_gauche.colliderect(barre_droite)

    # Si les barres sont à 20 pixels d'écart, augmenter le score lorsque la touche "espace" est enfoncée
    touches = pygame.key.get_pressed()
    #print("Barre gauche : " + str(barre_gauche.x) + " - Barre droite : " + str(barre_droite.x) + "--> " + str(abs(barre_gauche.right - barre_droite.left)))
    if collision or abs(barre_gauche.right - barre_droite.left) <= 100:
        if touches[pygame.K_SPACE] and not espace_appuye:
            score += 1
            espace_appuye = True
        elif not touches[pygame.K_SPACE]:
            espace_appuye = False
    else:
        # Réinitialiser le jeu si la touche "espace" est enfoncée au mauvais moment
        if touches[pygame.K_SPACE] and not espace_appuye:
            barre_gauche.x = 50
            barre_droite.x = largeur - 70
            score = 0
            compteur_collisions = 0
            espace_appuye = True
        elif not touches[pygame.K_SPACE]:
            espace_appuye = False

    # Déplacement des barres
    barre_gauche.x += vitesse_gauche
    barre_droite.x -= vitesse_droite

    # Remettre les barres à leur position initiale si elles sont en collision
    if collision:
        compteur_collisions += 1
        barre_gauche.x = 50
        barre_droite.x = largeur - 70

    # Effacement de l'écran
    fenetre.fill(BLANC)

    # Dessin des barres
    pygame.draw.rect(fenetre, NOIR, barre_gauche)
    pygame.draw.rect(fenetre, NOIR, barre_droite)

    # Affichage du compteur de collisions
    texte = font.render(f"Collisions : {compteur_collisions}", True, NOIR)
    fenetre.blit(texte, (10, 10))

    # Affichage du score
    texte_score = font.render(f"Score : {score}", True, NOIR)
    fenetre.blit(texte_score, (largeur - 160, 10))

    # Mise à jour de l'écran
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.delay(20)

# Quitter Pygame
pygame.quit()
sys.exit()
