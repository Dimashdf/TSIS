import pygame 
import sys
from pygame.locals import *
import random
import time

pygame.init()
FPS = 60
framepersec = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SPEED1 = 5
SCORE = 0
font = pygame.font.SysFont("Verdana", 60)
fontsmall = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME_OVER", True, BLACK)
road = pygame.image.load('racermaterials/ANimatedStreet.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer play")
screen.fill(WHITE)

class Silvercoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Image/silver.coin.png')
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        self.rect.move_ip(0, SPEED1)
        if self.rect.top > SCREEN_HEIGHT:
           
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class BronzeCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Image/bronze.png')
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    
    def move(self):
        self.rect.move_ip(0, SPEED1)
        if self.rect.top > SCREEN_HEIGHT:
           
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)







class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        self.rect.move_ip(0, SPEED1)
        if self.rect.top > SCREEN_HEIGHT:
           
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


  


class Foe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racermaterials/foe.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
           
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racermaterials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
F1 = Foe()
C1 = Coin()
S1 = Silvercoin()
B1 = BronzeCoin()

enemies = pygame.sprite.Group()
enemies.add(F1)
coin = pygame.sprite.Group()
coin.add(C1)
silver_coin = pygame.sprite.Group()
bronze_coin = pygame.sprite.Group()
silver_coin.add(S1)
bronze_coin.add(B1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(F1)
all_sprites.add(S1)
all_sprites.add(C1)
all_sprites.add(B1)




INC_SPEED = pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED, 1000)

moment_1 = False
moment_2 = False
moment_3 =False
while True:
    for event in pygame.event.get():
        if SCORE >3000 and not moment_1:
            SPEED += 3
            moment_1 = True
        if SCORE >5000 and not moment_2:
            SPEED += 5
            moment_2 = True

        if SCORE >10000 and not moment_3:
            SPEED += 5
            moment_3 = True
        
    
            
        #if event.type == INC_SPEED:
            #SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(road, (0, 0))
    scores = fontsmall.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
         pygame.mixer.Sound('racermaterials/crash.wav').play()
         time.sleep(0.5)

         screen.fill(RED)
         screen.blit(game_over, (30, 250))
         pygame.display.update()
         for entity in all_sprites:
               entity.kill()
         time.sleep(2)
         pygame.quit()
         sys.exit()
    if pygame.sprite.spritecollideany(P1, coin):
     SCORE += 100
     C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    if pygame.sprite.spritecollideany(P1,silver_coin):
         SCORE +=50
         S1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    if pygame.sprite.spritecollideany(P1,bronze_coin):
        SCORE+=25
        B1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)




    pygame.display.update()
    framepersec.tick(FPS)