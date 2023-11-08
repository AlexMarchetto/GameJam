import pygame,sys

class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.is_animating = True
        self.sprites = []
        for index in range(1, 4):
            image = pygame.image.load(f"player/player{index}.png")
            image = pygame.transform.scale(image, (128,128))
            self.sprites.append(image)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True
    
    
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.12

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]


pygame.init()
clock = pygame.time.Clock()
heightScreen = 400
widthScreen = 400
screen = pygame.display.set_mode((widthScreen,heightScreen))
pygame.display.set_caption("Sprite animator")

moving_sprites = pygame.sprite.Group()
player = Player(20,20)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)