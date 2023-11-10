import pygame, time, sys
from tile import AnimatedTile, StaticTile
from game_data import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player(AnimatedTile):
    def __init__(self, size, x, y, level):
        super().__init__(size, x, y, '../asset/player')
        self.rect.x = x
        self.rect.y = y
        self.move_speed = 32
        self.walls = level.walls_sprites
        self.level = level
        self.doors = level.doors_sprites
        self.is_moving = True       
        self.metronome_offset = 20
        self.surface = level.display_surface
        
        self.tolerance = level.tolerance
        self.beat_interval = self.level.beat_interval
        self.last_beat_time = 0
        self.beat_count = self.level.beat_count

        self.combo = 0
        self.motivation = 10
        

    #def game_over(self):

    def loose_motivation(self):
        self.motivation -= 2
        # if self.motivation <= 0:
            #game_over()    
        pygame.mixer.Channel(0).set_volume(1)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('../asset/sfx/hurt.mp3'))
        print(f"Motivation : {str(self.motivation).zfill(2)}", end='\r')

    def win_motivation(self):
        self.motivation += 1
        print(f"Motivation : {str(self.motivation).zfill(2)}", end='\r')

    def move(self, walls):
        

        key = pygame.key.get_pressed()
        new_rect = self.rect.copy()  # Créez le nouveau rectangle en dehors de la boucle
    
        if key[pygame.K_LEFT]:
            if self.is_moving:
                prediction = new_rect.x - self.move_speed
                if not self.check_collisions_walls(prediction,new_rect.y):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.x += self.move_speed
                    for sprite in self.level.walls_sprites:
                        sprite.rect.x += self.move_speed
                    for sprite in self.level.doors_sprites:
                        sprite.rect.x += self.move_speed
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.x += self.move_speed

                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_beat_time <= self.tolerance * 1000:
                        self.combo += 1
                    else:
                        self.combo = 0
                    print(f"Combo : {str(self.combo).zfill(2)}", end='\r')
                    
            self.is_moving = False

        if key[pygame.K_RIGHT] and self.is_moving:
            if self.is_moving:
                prediction = new_rect.x + self.move_speed
                if not self.check_collisions_walls(prediction,new_rect.y):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.x -= self.move_speed
                    for sprite in self.level.walls_sprites:
                        sprite.rect.x -= self.move_speed
                    for sprite in self.level.doors_sprites:
                        sprite.rect.x -= self.move_speed
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.x -= self.move_speed

                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_beat_time <= self.tolerance * 1000:
                        self.combo += 1
                    else:
                        self.combo = 0
                    print(f"Combo : {str(self.combo).zfill(2)}", end='\r')
                    # new_rect.x += 32
            self.is_moving = False   

        if key[pygame.K_UP]:
            if self.is_moving:
                prediction = new_rect.y - self.move_speed
                if not self.check_collisions_walls(new_rect.x,prediction):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.y += self.move_speed
                    for sprite in self.level.walls_sprites:
                        sprite.rect.y += self.move_speed
                    for sprite in self.level.doors_sprites:
                        sprite.rect.y += self.move_speed
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.y += self.move_speed


                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_beat_time <= self.tolerance * 1000:
                        self.combo += 1
                    else:
                        self.combo = 0
                    print(f"Combo : {str(self.combo).zfill(2)}", end='\r')
                    # new_rect.y -= 32
            self.is_moving = False

        if key[pygame.K_DOWN] and self.is_moving:
            if self.is_moving:
                prediction = new_rect.y + self.move_speed
                if not self.check_collisions_walls(new_rect.x,prediction):
                    for sprite in self.level.ground_sprites:
                        sprite.rect.y -= self.move_speed
                    for sprite in self.level.walls_sprites:
                        sprite.rect.y -= self.move_speed
                    for sprite in self.level.doors_sprites:
                        sprite.rect.y -= self.move_speed
                    for sprite in self.level.enemies_sprites:
                        sprite.rect.y -= self.move_speed


                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_beat_time <= self.tolerance * 1000:
                        self.combo += 1
                    else:
                        self.combo = 0
                    print(f"Combo : {str(self.combo).zfill(2)}", end='\r')
                    # new_rect.y += 32
            self.is_moving = False
               
        current_time = pygame.time.get_ticks()
        self.rect = new_rect


        if current_time - self.last_beat_time >= self.beat_interval:
            self.beat_count += 1
#            if self.beat_count % 2 == 0:
#                print("Temps fort de la musique ! /")
#            else:
#                print("Temps fort de la musique ! \\")

            # Mettez à jour le temps du dernier battement
            self.last_beat_time = current_time

            
        if not any(key):
            self.is_moving = True      

    def check_collisions_walls(self, player_next_move_x,player_next_move_y):
        for wall in self.walls:
            if  wall.rect.x == player_next_move_x and wall.rect.y == player_next_move_y:
                return True
        for index, door in enumerate(self.doors):
            if door.rect.x == player_next_move_x and door.rect.y == player_next_move_y:
                from level import Level
                if index == 5:
                    self.level.close()
                    level_1_1 = Level(trial_1_1, self.surface, 130, 3, 0.5)
                    level_1_1.run(self.surface)
                    pass
                elif index == 1:
                    # Code for index 1
                    pass
                elif index == 2:
                    # Code for index 2
                    pass
                elif index == 3:
                    # Code for index 3
                    pass
                elif index == 4:
                    # Code for index 4
                    pass
                
                print("Index de la porte :", index)
                return True
        for enemy in self.level.enemies_sprites:
            if enemy.rect.x == player_next_move_x and enemy.rect.y == player_next_move_y:
                self.loose_motivation()
                
                return True
        return False
    
    #def check_collisions_doors(self,player_next_move_x, player_next_move_y, doors):
    
    
            
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move(self.walls)
