import pygame
import sys
import pygame.mixer

# Définissez des valeurs par défaut
default_hauteur = 800
default_largeur = 800

# Vérifiez le nombre d'arguments
if len(sys.argv) == 1:
    # Si aucun argument n'est fourni, utilisez les valeurs par défaut
    WIDTH, HEIGHT = default_largeur, default_hauteur
elif len(sys.argv) == 3:
    # Si 2 arguments sont fournis, utilisez-les comme hauteur et largeur
    WIDTH, HEIGHT = int(sys.argv[1]), int(sys.argv[2])

pygame.init()

# Initialisation de Pygame Mixer
pygame.mixer.init()

# Charger la musique
pygame.mixer.music.load('audio.mp3')  # Remplacez 'votre_fichier_audio.mp3' par le nom de votre fichier audio

# Jouer la musique en boucle
pygame.mixer.music.play(-1)

# Taille de la grille (en fonction de la largeur et de la hauteur de la fenêtre)
grid_size = 10
grid_cell_size = min(WIDTH, HEIGHT) // grid_size

# Nombre de cases dans la grille
num_cells = grid_size

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Créez la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prototype de jeu")

# Position initiale du cercle (en haut à gauche de la grille)
circle_x = 0
circle_y = 0

# Position du bloc
block_x = 1
block_y = 1

# Vitesse de téléportation
teleport_distance = grid_cell_size

# Taille du cercle
circle_radius = 20

# Taille du bloc
block_width = grid_cell_size
block_height = grid_cell_size

# Couleur de la grille
GRID_COLOR = (200, 200, 200)

# Dictionnaire pour suivre l'état des touches
key_pressed = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for key in key_pressed.keys():
        if pygame.key.get_pressed()[key] and not key_pressed[key]:
            key_pressed[key] = True
            new_x, new_y = circle_x, circle_y
            if key == pygame.K_LEFT:
                new_x -= 1
            elif key == pygame.K_RIGHT:
                new_x += 1
            elif key == pygame.K_UP:
                new_y -= 1
            elif key == pygame.K_DOWN:
                new_y += 1

            # Vérifier si la nouvelle position est valide
            if 0 <= new_x < num_cells and 0 <= new_y < num_cells and not (new_x == block_x and new_y == block_y):
                circle_x, circle_y = new_x, new_y

                # Afficher les coordonnées du rond
                print(f"Coordonnées du rond : ({circle_x}, {circle_y})")

        if not pygame.key.get_pressed()[key]:
            key_pressed[key] = False

    # Dessiner la grille
    for x in range(0, WIDTH, grid_cell_size):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, grid_cell_size):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Dessiner le bloc
    block_rect = pygame.Rect(block_x * grid_cell_size, block_y * grid_cell_size, block_width, block_height)
    pygame.draw.rect(screen, BLUE, block_rect)

    # Dessiner le cercle du joueur
    circle_center_x = (circle_x + 0.5) * grid_cell_size
    circle_center_y = (circle_y + 0.5) * grid_cell_size
    pygame.draw.circle(screen, WHITE, (int(circle_center_x), int(circle_center_y)), circle_radius)

    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()
sys.exit()
