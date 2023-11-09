import pygame
import time
from tile import AnimatedTile
from random import randint

clock = pygame.time.Clock()

class Enemy(AnimatedTile):
    def __init__(self,size,x,y, to_bpm, walls):
        super().__init__(size,x,y,'../asset/enemy')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = size
        self.walls = walls
        self.to_bpm = to_bpm
    
    def move(self, walls, doors):
        if not self.will_collide(walls, doors):
            self.rect.x += self.speed
        
    def will_collide(self, walls, doors):
        future_rect = self.rect.copy()
        future_rect.x += self.speed
        temp_sprite = pygame.sprite.Sprite()
        temp_sprite.rect = future_rect
        if pygame.sprite.spritecollideany(temp_sprite, walls) or pygame.sprite.spritecollideany(temp_sprite, doors):
            return True
        return False
    
    def reverse_image(self): 
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image,True,False)
    
    def reverse(self):
        self.speed *= -1 
        
    def update(self, shift, walls, doors):
        self.rect.x += shift
        self.animate()
        self.move(walls, doors)
        self.reverse_image()