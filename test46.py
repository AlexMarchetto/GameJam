import pygame
import sys

pygame.init()

# Configuration de la fenêtre
width, height = 800, 600
cell_size = 50  # Taille d'une case
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Déplacement du cercle")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Position initiale du cercle (au centre de l'interface)
circle_radius = cell_size // 2
circle_x, circle_y = width // 2, height // 2

# Position de la grille (au centre de l'interface)
grid_x, grid_y = width // 2, height // 2

# Vitesse de déplacement
speed = cell_size

clock = pygame.time.Clock()

running = True
move_cooldown = 0  # Cooldown pour éviter un déplacement continu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if move_cooldown == 0:
        if keys[pygame.K_LEFT]:
            grid_x += cell_size
            move_cooldown = 10
        if keys[pygame.K_RIGHT]:
            grid_x -= cell_size
            move_cooldown = 10
        if keys[pygame.K_UP]:
            grid_y += cell_size
            move_cooldown = 10
        if keys[pygame.K_DOWN]:
            grid_y -= cell_size
            move_cooldown = 10

    move_cooldown = max(0, move_cooldown - 1)

    screen.fill(black)  # Fond noir

    # Dessin de la grille avec une case sur trois en bleu
    for x in range(grid_x - width // 2, width, cell_size):
        for y in range(grid_y - height // 2, height, cell_size):
            if (x // cell_size + y // cell_size) % 3 == 0:
                pygame.draw.rect(screen, blue, (x, y, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, white, (x, y, cell_size, cell_size))

    # Dessin du cercle centré dans sa case
    pygame.draw.circle(screen, white, (grid_x, grid_y), circle_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
