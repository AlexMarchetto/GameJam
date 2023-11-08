import pygame,sys
from settings import *
from level import Level
from game_data import level_1

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
bpm = 50
level = Level(level_1, screen, bpm)

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
    level.run()

    pygame.display.update()
    clock.tick(60)