import pygame

class ProgressBar:
    def __init__(self, screen, total_time, width=600, height=40, x=100, color=(0, 255, 0)):
        self.screen = screen
        self.total_time = total_time
        self.width = width
        self.height = height
        self.x = (screen.get_width() - width) // 2
        self.y = 20  # Ajuster la position verticale pour la mettre en haut
        self.color = color
        self.progress = 0.0

    def update(self):
        time_elapsed = pygame.time.get_ticks() / 1000
        self.progress = min(time_elapsed / self.total_time, 1.0)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width * self.progress, self.height))
