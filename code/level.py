import pygame 
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tile import StaticTile
from enemy import Enemy
from player import Player

class Level:
    def __init__(self, level_data, surface, bpm):
        # General setup
        self.display_surface = surface
        self.world_shift = 0
        self.beat_interval = (60000 / (bpm*1/60)) * 2
        self.last_beat_time = 0
        self.beat_count = 0


        # Ground setup
        grounds_layout = import_csv_layout(level_data['ground'])
        self.ground_sprites = self.create_tile_group(grounds_layout, 'ground')

        # walls setup
        walls_layout = import_csv_layout(level_data['walls'])
        self.walls_sprites = self.create_tile_group(walls_layout, 'walls')

        # doors setup
        doors_layout = import_csv_layout(level_data['doors'])
        self.doors_sprites = self.create_tile_group(doors_layout, 'doors')

        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player_sprites = self.create_tile_group(player_layout, 'player' )
        # enemies
        enemies_layout = import_csv_layout(level_data['enemies'])
        self.enemies_sprites = self.create_tile_group(enemies_layout, 'enemies')



    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()
 

        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'ground':
                        ground_tile_list = import_cut_graphics('../asset/Tileset/ground.png')
                        tile_surface = ground_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        
                    
                    if type == 'walls':
                        walls_tile_list = import_cut_graphics('../asset/Tileset/walls.png')
                        tile_surface = walls_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                  

                    if type == 'doors':
                        doors_tile_list = import_cut_graphics('../asset/Tileset/doors.png')
                        tile_surface = doors_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                       

                    if type == 'player':
                        self.player = Player(tile_size, x, y, self.walls_sprites, self)
                        sprite = self.player 

                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y,self.beat_interval)
                    
                    sprite_group.add(sprite)

        return sprite_group
    
    def enemy_collision_reverse(self):
        for enemy in self.enemies_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.walls_sprites,False) or pygame.sprite.spritecollide(enemy,self.doors_sprites,False):
                enemy.reverse()
                            
                

    def run(self, surface):
        self.ground_sprites.update(self.world_shift)
        self.ground_sprites.draw(surface)

        self.walls_sprites.update(self.world_shift)
        self.walls_sprites.draw(surface)

        self.doors_sprites.update(self.world_shift)
        self.doors_sprites.draw(surface)

        self.player_sprites.update(self.world_shift)
        self.player_sprites.draw(surface)

        self.enemies_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        
        self.enemies_sprites.draw(surface)

        

        
        
