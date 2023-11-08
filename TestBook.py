import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Empêcher le personnage d'aller sur certaines tuiles")

# Créez une classe pour représenter le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1

    def update(self, collidable_tiles):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            for tile in collidable_tiles:
                if self.rect.colliderect(tile):
                    self.rect.x += self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            for tile in collidable_tiles:
                if self.rect.colliderect(tile):
                    self.rect.x -= self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            for tile in collidable_tiles:
                if self.rect.colliderect(tile):
                    self.rect.y += self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            for tile in collidable_tiles:
                if self.rect.colliderect(tile):
                    self.rect.y -= self.speed

# Créez une liste de tuiles collidables
collidable_tiles = [pygame.Rect(200, 200, 30, 30), pygame.Rect(300, 300, 30, 30), pygame.Rect(400, 400, 30, 30)]

# Créez le joueur
player = Player(screen_width // 2, screen_height // 2)

# Dans la boucle de jeu principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour du joueur en fonction des collisions
    player.update(collidable_tiles)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), collidable_tiles[0])  # Dessinez les tuiles collidables
    pygame.draw.rect(screen, (0, 0, 0), collidable_tiles[1])
    pygame.draw.rect(screen, (0, 0, 0), collidable_tiles[2])
    pygame.draw.rect(screen, (255, 0, 0), player.rect)  # Dessinez le joueur

    pygame.display.flip()

pygame.quit()
sys.exit()
