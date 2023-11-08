import pygame
import csv

#Initialisez Pygame
pygame.init()

#Dimensions de la fenêtre
screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Créer des murs depuis un fichier CSV")

#Créez une classe pour représenter les murs
class Wall(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 0))  # Couleur des murs (noir dans cet exemple)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

#Créez une fonction pour charger les données depuis un fichier CSV et générer les murs
def load_walls_from_csv(file_path):
    wall_group = pygame.sprite.Group()

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row_index, row in enumerate(csv_reader):
                for col_index, cell in enumerate(row):
                    if cell == '1' or cell == '2' or cell == '3'or cell == '4' or cell == '5' or cell == '6' or cell == '7' or cell == '8' or cell == '8' or cell == '10' or cell == '11' or cell == '12'or cell == '13'or cell == '14'or cell == '15'or cell == '16'or cell == '17'or cell == '18'or cell == '19'or cell == '20'or cell == '21'or cell == '22':  # Vous pouvez utiliser un autre caractère ou numéro pour les murs
                        wall = Wall(col_index * 32, row_index * 32)
                        wall_group.add(wall)

    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")

    return wall_group

#Chargez les données du fichier CSV et créez les murs
wall_group = load_walls_from_csv('../levels/1/level1_walls.csv')

#Dans la boucle de jeu principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    wall_group.draw(screen)

    pygame.display.flip()

pygame.quit()