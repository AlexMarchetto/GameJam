import pygame
import time
from tile import AnimatedTile
from random import randint

clock = pygame.time.Clock()

class Enemy(AnimatedTile):
    def __init__(self,size,x,y, to_bpm, walls, doors, level):
        super().__init__(size,x,y,'../asset/enemy')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = size
        self.walls = walls
        self.doors = doors
        self.to_bpm = to_bpm
        self.player = level.player_sprites
        self.level = level
        self.last_move_time = pygame.time.get_ticks()
    
    def move(self, walls, doors):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_move_time

        if elapsed_time >= self.to_bpm:
            if not self.will_collide(walls, doors):
                self.rect.x += self.speed
                self.last_move_time = current_time

            
        
        
    def will_collide(self, walls, doors):
        future_rect = self.rect.copy()
        future_rect.x += self.speed
        temp_sprite = pygame.sprite.Sprite()
        temp_sprite.rect = future_rect
        if pygame.sprite.spritecollideany(temp_sprite, walls) or pygame.sprite.spritecollideany(temp_sprite, doors):
            return True
        if pygame.sprite.spritecollideany(temp_sprite, self.player):
            player = self.level.player
            player.loose_motivation()
            return True
        return False
    
    def reverse_image(self): 
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image,True,False)
    
    def reverse(self):
        self.speed *= -1 
        
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move(self.walls, self.doors)
        self.reverse_image()