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
    
    def move(self, walls, to_bmp):
        
        new_rect = self.rect.copy()
        prediction = new_rect.x - 32

        if not self.check_collisions(prediction,new_rect.y, walls):
            new_rect.x -= 32
        self.rect.x += self.speed
    
    def check_collisions(self, enemy_next_move_x,enemy_next_move_y, walls):
        for wall in walls:
            if  wall.rect.x == enemy_next_move_x and wall.rect.y == enemy_next_move_y:
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
        self.move(self.walls,self.to_bpm)
        self.reverse_image()