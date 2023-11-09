import pygame,sys
from settings import *
from level import Level
from game_data import level_1
from button import Button

pygame.init()
SCREEN = pygame.display.set_mode((screen_width,screen_height))
BG = pygame.image.load("../asset/BackgroundMenu.png")
GAME_NAME = "School'n'Beats"
pygame.display.set_caption(GAME_NAME)

pygame.mixer.music.load("../asset/musics/Menu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

clock = pygame.time.Clock()
bpm = 50
level = Level(level_1, SCREEN, bpm)

# Créer la surface du jeu
game_surface = pygame.Surface((screen_width, screen_height))

def get_font(size):
    return pygame.font.Font("../asset/MerchantCopy.ttf", size)

def play(difficulty):
    pygame.display.set_caption(GAME_NAME)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            SCREEN.fill('black')
            level.run(game_surface)

            zoomed_surface = pygame.transform.scale(game_surface, (screen_width*5, screen_height*5))
            SCREEN.blit(zoomed_surface, (0, 0))

            pygame.display.update()
            clock.tick(60)

def select_dificulty():
    pygame.display.set_caption(GAME_NAME)

    while True:
        SCREEN.blit(BG,(0,0))

        DIFFICULTY_MOUSE_POS = pygame.mouse.get_pos()

        DIFFICULTY_TEXT = get_font(150).render("Choisissez votre difficultée !", True, "#b68f40")
        DIFFICULTY_RECT = DIFFICULTY_TEXT.get_rect(center=(960,200))

        DIFFICULTY_FACILE_BUTTON_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(960,400), text_input="FACILE", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        DIFFICULTY_MOYEN_BUTTON_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(960,550), text_input="MOYEN", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        DIFFICULTY_DUR_BUTTON_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(960,700), text_input="DUR", font=get_font(100), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(DIFFICULTY_TEXT,DIFFICULTY_RECT)

        for button in [DIFFICULTY_FACILE_BUTTON_BUTTON, DIFFICULTY_MOYEN_BUTTON_BUTTON, DIFFICULTY_DUR_BUTTON_BUTTON]:
            button.changeColor(DIFFICULTY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DIFFICULTY_FACILE_BUTTON_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):                    
                    play(1)
                if DIFFICULTY_MOYEN_BUTTON_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
                    play(2)
                if DIFFICULTY_DUR_BUTTON_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
                    play(3)

        pygame.display.update()

def credit():
    pygame.display.set_caption(GAME_NAME)

    while True:
        SCREEN.blit(BG,(0,0))

        CREDIT_MOUSE_POS = pygame.mouse.get_pos()

        CREDIT_TEXT = get_font(150).render("Crédits", True, "#b68f40")
        CREDIT_RECT = CREDIT_TEXT.get_rect(center=(960,200))

        MENU_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(960,900), text_input="MENU", font=get_font(150), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(CREDIT_TEXT,CREDIT_RECT)
        MENU_BUTTON.changeColor(CREDIT_MOUSE_POS)
        MENU_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(CREDIT_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def main_menu():
    pygame.display.set_caption(GAME_NAME)

    while True:
        SCREEN.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(150).render("School'n'Beats", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(960,200))

        PLAY_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(960,400), text_input="JOUER", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        CREDIT_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(960,550), text_input="CREDITS", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(960,700), text_input="QUITTER", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT,MENU_RECT)

        for button in [PLAY_BUTTON, CREDIT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_dificulty()
                if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
