import pygame
from tile import AnimatedTile, StaticTile


class Player(AnimatedTile):
    def __init__(self, size, x, y, walls, level):
        from level import Level
        super().__init__(size, x, y, '../asset/player')
        self.rect.x = x
        self.rect.y = y
        self.walls = walls
        self.level = level
        self.is_moving = True
        

    def move(self, walls):
        

        key = pygame.key.get_pressed()
        new_rect = self.rect.copy()  # Créez le nouveau rectangle en dehors de la boucle
    
        if key[pygame.K_LEFT] and self.is_moving:
            if self.is_moving:
                prediction = new_rect.x - 32
                if not self.check_collisions(prediction,new_rect.y, walls):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.x += 32
                    for sprite in self.level.walls_sprites:
                        sprite.rect.x += 32
                    for sprite in self.level.doors_sprites:
                        sprite.rect.x += 32
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.x += 32
                    # new_rect.x -= 32
            self.is_moving = False

        if key[pygame.K_RIGHT] and self.is_moving:
            if self.is_moving:
                prediction = new_rect.x + 32
                if not self.check_collisions(prediction,new_rect.y, walls):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.x -= 32
                    for sprite in self.level.walls_sprites:
                        sprite.rect.x -= 32
                    for sprite in self.level.doors_sprites:
                        sprite.rect.x -= 32
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.x -= 32
                    # new_rect.x += 32
            self.is_moving = False   

        if key[pygame.K_UP]:
            if self.is_moving:
                prediction = new_rect.y - 32
                if not self.check_collisions(new_rect.x,prediction, walls):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.y += 32
                    for sprite in self.level.walls_sprites:
                        sprite.rect.y += 32
                    for sprite in self.level.doors_sprites:
                        sprite.rect.y += 32
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.y += 32
                    # new_rect.y -= 32
            self.is_moving = False

        if key[pygame.K_DOWN] and self.is_moving:
            if self.is_moving:
                prediction = new_rect.y + 32
                if not self.check_collisions(new_rect.x,prediction, walls):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.y -= 32
                    for sprite in self.level.walls_sprites:
                        sprite.rect.y -= 32
                    for sprite in self.level.doors_sprites:
                        sprite.rect.y -= 32
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.y -= 32
                    # new_rect.y += 32
            self.is_moving = False
               
        self.rect = new_rect

        if not any(key):
            self.is_moving = True

        
        

    def check_collisions(self, player_next_move_x,player_next_move_y, walls):
        for wall in walls:
            if  wall.rect.x == player_next_move_x and wall.rect.y == player_next_move_y:
                return True

        return False
            
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move(self.walls)
        
       