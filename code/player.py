import pygame
from tile import AnimatedTile, StaticTile

class Player(AnimatedTile):
    def __init__(self, size, x, y, walls):
        super().__init__(size, x, y, '../asset/player')
        self.rect.x = x
        self.rect.y = y
        self.walls = walls

        

    def move(self, walls):
        key_pressed = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

        key = pygame.key.get_pressed()
        new_rect = self.rect.copy()  # Créez le nouveau rectangle en dehors de la boucle

        for key in key_pressed.keys():

            if pygame.key.get_pressed()[key]:
                key_pressed[key] = True
                if key == pygame.K_LEFT:
                    prediction = new_rect.x - 32
                    if not self.check_collisions(prediction,new_rect.y, walls):
                        new_rect.x -= 32
                if key == pygame.K_RIGHT:
                    prediction = new_rect.x + 32
                    if not self.check_collisions(prediction,new_rect.y, walls):
                        new_rect.x += 32
                if key == pygame.K_UP:
                    prediction = new_rect.y - 32
                    if not self.check_collisions(new_rect.x,prediction, walls):
                        new_rect.y -= 32
                if key == pygame.K_DOWN:
                    prediction = new_rect.y + 32
                    if not self.check_collisions(new_rect.x,prediction, walls):
                        new_rect.y += 32

        self.rect = new_rect
                                   
    def check_collisions(self, player_next_move_x,player_next_move_y, walls):
        for wall in walls:
            if  wall.rect.x == player_next_move_x and wall.rect.y == player_next_move_y:
                return True

        return False
            
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move(self.walls)
        
       