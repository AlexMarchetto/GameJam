import pygame
import sys
import pygame.mixer
import pygame.time
import random
import os
from ProgressBar import ProgressBar
from Book import Book

# Paramètres du jeu
BPM = 128  # Battements par minute
TOLERANCE = 0.225  # Seuil de tolérance en secondes

# Autres paramètres du jeu
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

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialisation de Pygame Mixer
pygame.mixer.init()

# Charger la musique
pygame.mixer.music.load('audio.mp3')

# Jouer la musique en boucle
pygame.mixer.music.play(-1)

# Taille de la grille (en fonction de la largeur et de la hauteur de la fenêtre)
grid_size = 10
grid_cell_size = min(WIDTH, HEIGHT) // grid_size

# Nombre de cases dans la grille
num_cells = grid_size

c1=Book(screen,200,200,"book2.png")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)

# Création de la barre de progression
progress_bar = ProgressBar(screen, total_time=30, width=600, height=20, x=(WIDTH - 600) // 2, color=RED)

# Créez la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prototype de jeu")

# Position initiale du cercle (en haut à gauche de la grille)
circle_x = 0
circle_y = 0

# Liste des blocs
blocks = []

class Block:
    def __init__(self, x, y, block_type):
        self.x = x
        self.y = y
        self.type = block_type

# Ajoutez des blocs avec un exemple de bloc mur
blocks.append(Block(1, 1, "mur"))

# Taille du cercle
circle_radius = 20

# Couleur de la grille
GRID_COLOR = (200, 200, 200)

# Dictionnaire pour suivre l'état des touches
key_pressed = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

# Calculer l'intervalle de battement
beat_interval = 60000 / BPM  # 60000 ms (1 minute) divisé par le BPM

# Suivre le temps du dernier battement
last_beat_time = 0

# Variable pour suivre le temps fort de la musique
beat_count = 0

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
            if 0 <= new_x < num_cells and 0 <= new_y < num_cells and all(
                (new_x != block.x or new_y != block.y) for block in blocks
            ):
                circle_x, circle_y = new_x, new_y

                # Afficher les coordonnées du rond
                # print(f"Coordonnées du rond : ({circle_x}, {circle_y})")

                # Obtenir le temps actuel
                current_time = pygame.time.get_ticks()

                # Vérifier si l'appui est dans les temps
                if current_time - last_beat_time <= TOLERANCE * 1000:
                    print("Dans les temps !")
                else:
                    print("Trop tôt ou trop tard.")

        if not pygame.key.get_pressed()[key]:
            key_pressed[key] = False

    # Obtenir le temps actuel
    current_time = pygame.time.get_ticks()

    # Vérifier le temps fort de la musique
    if current_time - last_beat_time >= beat_interval:
        beat_count += 1
        if beat_count % 2 == 0:
            print("Temps fort de la musique ! /")
        else:
            print("Temps fort de la musique ! \\")

        # Mettez à jour le temps du dernier battement
        last_beat_time = current_time

    # Dessiner la grille
    for x in range(0, WIDTH, grid_cell_size):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, grid_cell_size):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Dessiner les blocs
    for block in blocks:
        if block.type == "mur":
            block_rect = pygame.Rect(
                block.x * grid_cell_size, block.y * grid_cell_size, grid_cell_size, grid_cell_size
            )
            pygame.draw.rect(screen, BLUE, block_rect)

    # Dessiner le cercle du joueur
    circle_center_x = (circle_x + 0.5) * grid_cell_size
    circle_center_y = (circle_y + 0.5) * grid_cell_size
    pygame.draw.circle(screen, WHITE, (int(circle_center_x), int(circle_center_y)), circle_radius)
    
    c1.draw()

    pygame.display.update()
    progress_bar.update()
    # Vérification si le temps est terminé
    if progress_bar.progress >= 1.0:
        running = False
    screen.fill((0, 0, 0))
    progress_bar.draw()

pygame.quit()
os.system("python main.py")
sys.exit()
