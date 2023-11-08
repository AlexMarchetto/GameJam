import pygame
import time
from tile import AnimatedTile
from random import randint

clock = pygame.time.Clock()

class Enemy(AnimatedTile):
    def __init__(self,size,x,y, to_bpm):
        super().__init__(size,x,y,'../asset/enemy')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = size
        self.to_bpm = to_bpm
    
    def move(self):
        self.rect.x += self.speed
        clock.tick(self.to_bpm)
    
    def reverse_image(self): 
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image,True,False)
    
    def reverse(self):
        self.speed *= -1 
        
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        #self.move()
        self.reverse_image()