import pygame,sys, argparse
from settings import *
from level import Level
from game_data import *
from button import Button
from ProgressBar import ProgressBar

parser = argparse.ArgumentParser(description="School'N'Beats est un jeu de rythme créé dans le cadre d'une GameJam organisée par l'IUT.")


# Add arguments
parser.add_argument('screen_width', type=int, nargs='?', default=1920, help='Largeur de la fenêtre (default: 1920)')
parser.add_argument('screen_height', type=int, nargs='?', default=1080, help="Auteur de la fenêtre (default: 1080)")
parser.add_argument('--tol', type=float, default=0.35, help='Tolerance value (default: 0.35), tolérance plus basse = plus dur. TOL > 0')

args = parser.parse_args()

# Set the entered information using sys.argv
sys.argv[1:] = [str(args.screen_width), str(args.screen_height), '--tol', str(args.tol)]

print("Tolerance:", args.tol)

screen_width, screen_height = args.screen_width, args.screen_height
tolerance = args.tol

pygame.init()
SCREEN = pygame.display.set_mode((screen_width,screen_height))
BG = pygame.image.load("../asset/BackgroundMenu.png")
GAME_NAME = "School'n'Beats"
pygame.display.set_caption(GAME_NAME)

pygame.mixer.music.load("../asset/musics/Menu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

clock = pygame.time.Clock()
bpm = 82.5
difficulty = 3


# Créer la surface du jeu
game_surface = pygame.Surface((screen_width, screen_height))

def get_font(size):
    return pygame.font.Font("../asset/MerchantCopy.ttf", size)

def splas_screen():
        pygame.display.set_caption(GAME_NAME)
        SCREEN.blit(BG,(0,0))

def play(difficulty):
    pygame.display.set_caption(GAME_NAME)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("../asset/musics/Level1.mp3")
    pygame.mixer.music.play(-1)
    level = Level(level_1, SCREEN, bpm, difficulty, tolerance)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill('black')
        level.run(game_surface)

        zoomed_surface = pygame.transform.scale(game_surface, (screen_width*5, screen_height*5))
        SCREEN.blit(zoomed_surface, (-(32*47),-(32*85)))
        #SCREEN.blit(zoomed_surface, (0,0))

        pygame.display.update()
        clock.tick(60)

def select_dificulty():
    pygame.display.set_caption(GAME_NAME)

    while True:
        SCREEN.blit(BG,(0,0))

        DIFFICULTY_MOUSE_POS = pygame.mouse.get_pos()

        DIFFICULTY_TEXT = get_font(100).render("Choisissez votre difficultée !", True, "#b68f40")
        DIFFICULTY_RECT = DIFFICULTY_TEXT.get_rect(center=(screen_width/2,screen_height/6))

        DIFFICULTY_FACILE_BUTTON_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(screen_width/2,400), text_input="FACILE", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        DIFFICULTY_MOYEN_BUTTON_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(screen_width/2,550), text_input="MOYEN", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        DIFFICULTY_DUR_BUTTON_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(screen_width/2,700), text_input="DUR", font=get_font(100), base_color="#d7fcd4", hovering_color="White")

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
        CREDIT_RECT = CREDIT_TEXT.get_rect(center=(screen_width/2,200))

        CREDIT_TEXT2 = get_font(150).render("Créer par Nacer, Angel and Alex", True, "#1d8738")
        CREDIT_RECT2 = CREDIT_TEXT2.get_rect(center=(screen_width/2,500))

        CREDIT_TEXT3 = get_font(150).render("Font : Merchant Copy", True, "#1d8738")
        CREDIT_RECT3 = CREDIT_TEXT2.get_rect(center=(screen_width/2,600))

        MENU_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(screen_width/2,900), text_input="MENU", font=get_font(150), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(CREDIT_TEXT,CREDIT_RECT)
        SCREEN.blit(CREDIT_TEXT2,CREDIT_RECT2)
        SCREEN.blit(CREDIT_TEXT3,CREDIT_RECT3)
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

def rules_menu():
    pygame.display.set_caption(GAME_NAME)
    while True:
        SCREEN.blit(BG,(0,0))

        RULES_MOUSE_POS = pygame.mouse.get_pos()

        RULES_TEXT = get_font(150).render("REGLES", True, "#b68f40")
        RULES_RECT = RULES_TEXT.get_rect(center=(screen_width/2,100))

        R1_TEXT = get_font(40).render("Dans ce jeu palpitant, vous devrez naviguer a travers les couloirs animes de l'IUT2 au son de la musique,", True, "#FFFFFF")
        R1_RECT = R1_TEXT.get_rect(center=(screen_width/2,250))

        R2_TEXT = get_font(40).render("tout en collectant un nombre defini de cours eparpilles sur la carte.", True, "#FFFFFF")
        R2_RECT = R2_TEXT.get_rect(center=(screen_width/2,310))

        R3_TEXT = get_font(40).render("Cependant, gardez toujours le rythme,", True, "#FFFFFF")
        R3_RECT = R3_TEXT.get_rect(center=(screen_width/2,370))

        R4_TEXT = get_font(40).render("car votre niveau de motivation depend de votre synchronisation parfaite avec la mélodie envoutante qui vous accompagne.", True, "#FFFFFF")
        R4_RECT = R4_TEXT.get_rect(center=(screen_width/2,430))

        R5_TEXT = get_font(40).render("Les collisions avec d'autres etudiants sont a eviter a tout prix, car cela pourrait egalement saper votre enthousiasme.", True, "#FFFFFF")
        R5_RECT = R5_TEXT.get_rect(center=(screen_width/2,490))

        R6_TEXT = get_font(40).render("Si votre motivation atteint le triste score de zero,", True, "#FFFFFF")
        R6_RECT = R6_TEXT.get_rect(center=(screen_width/2,550))

        R7_TEXT = get_font(40).render("ou si le temps imparti s'ecoule avant que vous n'ayez amassé tous les cours necessaires,", True, "#FFFFFF")
        R7_RECT = R7_TEXT.get_rect(center=(screen_width/2,610))

        R8_TEXT = get_font(40).render("la partie sera malheureusement terminee.", True, "#FFFFFF")
        R8_RECT = R8_TEXT.get_rect(center=(screen_width/2,670))

        R9_TEXT = get_font(40).render("Le deplacement sur la carte s'effectue avec les fleches directionelles du clavier", True, "#FFFFFF")
        R9_RECT = R9_TEXT.get_rect(center=(screen_width/2,720))

        R10_TEXT = get_font(40).render("Bonne chance !", True, "#FFFFFF")
        R10_RECT = R10_TEXT.get_rect(center=(screen_width/2,800))

        MENU_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(960,930), text_input="MENU", font=get_font(150), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(RULES_TEXT,RULES_RECT)
        SCREEN.blit(R1_TEXT,R1_RECT)
        SCREEN.blit(R2_TEXT,R2_RECT)
        SCREEN.blit(R3_TEXT,R3_RECT)
        SCREEN.blit(R4_TEXT,R4_RECT)
        SCREEN.blit(R5_TEXT,R5_RECT)
        SCREEN.blit(R6_TEXT,R6_RECT)
        SCREEN.blit(R7_TEXT,R7_RECT)
        SCREEN.blit(R8_TEXT,R8_RECT)
        SCREEN.blit(R9_TEXT,R9_RECT)
        SCREEN.blit(R10_TEXT,R10_RECT)

        MENU_BUTTON.changeColor(RULES_MOUSE_POS)
        MENU_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(RULES_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption(GAME_NAME)

    while True:
        SCREEN.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(150).render("School'n'Beats", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_width/2,200))

        PLAY_BUTTON = Button(image=pygame.image.load("../asset/Button.png"), pos=(screen_width/2,400), text_input="JOUER", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        CREDIT_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(screen_width/2,550), text_input="CREDITS", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(screen_width/2,850), text_input="QUITTER", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        RULES_BUTTON = Button(image=pygame.image.load("../asset/Button.png"),pos=(screen_width/2,700), text_input="REGLES", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT,MENU_RECT)

        for button in [PLAY_BUTTON, CREDIT_BUTTON, QUIT_BUTTON,RULES_BUTTON]:
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
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
