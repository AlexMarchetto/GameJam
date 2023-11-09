import pygame
import time

# Initialisation de Pygame
pygame.init()

# Paramètres du métronome
bpm = 83  # Tempo en battements par minute
beat_interval = 60 / bpm  # Intervalle entre chaque temps fort en secondes

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialisation de la fenêtre Pygame
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Metronome')

# Horloge Pygame
clock = pygame.time.Clock()

# Variables pour contrôler l'affichage du carré noir
show_square = False
last_beat_time = time.time()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vérifie le temps écoulé depuis le dernier temps fort
    elapsed_time = time.time() - last_beat_time

    # Si l'intervalle est atteint, bascule l'affichage du carré noir
    if elapsed_time >= beat_interval:
        show_square = not show_square
        last_beat_time = time.time()

    # Efface l'écran
    screen.fill(WHITE)

    # Affiche le carré noir si nécessaire
    if show_square:
        square_size = 50
        square_rect = pygame.Rect((width - square_size) // 2, (height - square_size) // 2, square_size, square_size)
        pygame.draw.rect(screen, BLACK, square_rect)

    # Met à jour l'affichage
    pygame.display.flip()


# Quitte Pygame
pygame.quit()
