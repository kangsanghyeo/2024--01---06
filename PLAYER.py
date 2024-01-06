import pygame as pg
from PLAY_settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        ##############
        self.sprite_sheet = pg.image.load("alien.png").convert()
        self.sprite_width = 32
        self.sprite_height = 32
        self.sprite_columns = 6
        self.current_frame = 0
        
        self.image = pg.Surface((self.sprite_width, self.sprite_height))

        rect = (self.sprite_width*self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(pg.Color(255, 0, 255))
 
        self.rect = self.image.get_rect() 
        self.rect.center = (WIDTH/2, HEIGHT/2) 

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
    def calc_next_frame(self):
        tick = pg.time.get_ticks()
        if tick - self.elapsed > self.threshold:
            self.elapsed = tick
            if self.current_frame == self.sprite_columns:
                self.current_frame = 0
            else:
                self.current_frame += 1
                
    def jumping(self):
        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.blockforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.floorforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

        self.rect.y += 0.1
        hits = pg.sprite.spritecollide(self, self.game.squareforms, False)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x*PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        rect = (self.sprite_width*self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(pg.Color(255, 0, 255))
        
        self.rect.midbottom = self.pos
        
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Blockform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Floorform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill((0, 0, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Squareform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
