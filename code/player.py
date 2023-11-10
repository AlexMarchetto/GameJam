import pygame, time, sys
from tile import AnimatedTile, StaticTile


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player(AnimatedTile):
    def __init__(self, size, x, y, walls, level, surface, tolerance):
        from level import Level
        super().__init__(size, x, y, '../asset/player')
        self.rect.x = x
        self.rect.y = y
        self.move_speed = 32
        self.walls = walls
        self.level = level
        self.is_moving = True       
        self.metronome_offset = 20
        self.surface = surface
        
        self.tolerance = tolerance
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
                if not self.check_collisions(prediction,new_rect.y, walls):
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
                if not self.check_collisions(prediction,new_rect.y, walls):
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
                if not self.check_collisions(new_rect.x,prediction, walls):
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
                if not self.check_collisions(new_rect.x,prediction, walls):
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

    def check_collisions(self, player_next_move_x,player_next_move_y, walls):
        for wall in walls:
            if  wall.rect.x == player_next_move_x and wall.rect.y == player_next_move_y:
                return True
        return False
    
    
            
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move(self.walls)
