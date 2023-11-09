import pygame

class Book:
    def __init__(self,screen,x,y,file="book1.png",width=20, height=20):
        self.screen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image = pygame.image.load(file) 
        self.isFounded=False

    def draw(self):
        if not(self.isFounded):
           self.screen.blit(self.image,(self.x,self.y))

    def setTrueIsFounded(self):
        self.isFounded=True

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

