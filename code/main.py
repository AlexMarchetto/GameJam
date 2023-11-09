import pygame,sys
from settings import *
from level import Level
from game_data import level_1

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
bpm = 50
level = Level(level_1, screen, bpm)

# Créer la surface du jeu
game_surface = pygame.Surface((screen_width, screen_height))

# Charger la musique
pygame.mixer.music.load('../audio.mp3')

# Jouer la musique en boucle
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    level.run(game_surface)

    zoomed_surface = pygame.transform.scale(game_surface, (screen_width*5, screen_height*5))
    screen.blit(zoomed_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)