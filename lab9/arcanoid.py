# Add your imports here
import pygame
from pygame import draw
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 960, 600
screen = pygame.display.set_mode((width, height))
fon = pygame.image.load('fon.png')
fon = pygame.transform.scale(fon, (960, 600))
arial_50 = pygame.font.SysFont('arial', 50)

pygame.display.set_caption("Game menu")

# Add your fonts and Menu class here
class Menu:
    def __init__(self):
        self.option_surfaces = []
        self.callbacks = []
        self.current_option_index = 0

    def append_option(self, option, callback):
        self.option_surfaces.append(arial_50.render(option, True, (0, 0, 0)))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.option_surfaces) - 1))

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, option_y):
        for i, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y)
            if i == self.current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

# Initialize the menu
menu = Menu()
menu.append_option("Play game", lambda: start_game())
menu.append_option("Options", lambda: print("options"))
menu.append_option('Quit', quit)

# Initialize game variables
running = False
W, H = 1000, 700
FPS = 60
# Add your game setup code here

# Function to start the game
def start_game():
    global running
    running = True

# Main game loop
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu.switch(-1)
            elif event.key == pygame.K_s:
                menu.switch(1)
            elif event.key == pygame.K_SPACE:
                menu.select()

    screen.fill((0, 0, 0))
    screen.blit(fon, (0, 0))
    menu.draw(screen, 100, 75, 100)
    pygame.display.flip()

# Add your game logic here
W, H = 1000, 700
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
#переменные, связанные с изменением во времени
timer1 = 0
timer2 = 0
change_period = 3


done = False
bg = (0, 0, 0)

#весло
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#мячик
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1 #задает начальное направление движения мяча по горизонтали (dx = 1, вправо) и вертикали (dy = -1, вверх).

#счет игры 
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#загружаем музыки которые мы будем использывать 
collision_sound = pygame.mixer.Sound('ackanoid_catch.mp3')
special_collision_sound = pygame.mixer.Sound('ackanoid_specialcatch.wav')
boom_collision_sound = pygame.mixer.Sound('ackanoid_boom.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

#функции, которые со временем меняют скорость мяча и размер ракетки
def change_ball_speed(change_period):
    global ballSpeed, timer1
    if timer1 >= change_period:
        timer1 = 0
        ballSpeed += 3

def change_paddle_size(change_period):
    global paddle, timer2
    if timer2 >= change_period:
        timer2 = 0
        #сохранение соотношения сторон весла
        aspect_ratio = paddle.width / paddle.height
        width = paddle.width - 15
        height = width / aspect_ratio
        paddle = pygame.Rect(paddle.left, paddle.top, width, height)


#настройка блока
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

#выбор специальных блоков из block_list и color_list
num_special = num_unbreakable = random.randint(4,7)
special_list = [(color_list[i], block_list[i]) for i in (random.randrange(0,40) for j in range(num_special))]
special_color_list = [pair[0] for pair in special_list]
special_block_list = [pair[1] for pair in special_list]

#выбор того же количества неразрушимых блоков, что и количества специальных блоков
#не совсем то же самое - число может быть меньше, если выбранный прямоугольник уже отнесен к специальной группе)
unbreakable_list = [(color_list[i], block_list[i]) for i in (random.randrange(0,40) for j in range(num_unbreakable)) if block_list[i] not in special_block_list]
unbreakable_color_list = [pair[0] for pair in unbreakable_list]
unbreakable_block_list = [pair[1] for pair in unbreakable_list]

#экран проигрыша
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Экран победы
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#вер за помощью. когда игра входит в цикл, игрок может поместить мяч в середину
#но ценой +2 скорости для мяча
help_used = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    #чертежные блоки
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)
     if (color_list[color], block) not in special_list and (color_list[color], block) not in unbreakable_list]
    
    #добавляем круг для специальных блоков 
    for special_color, special_block in special_list:
        pygame.draw.rect(screen, special_color, special_block)
        pygame.draw.circle(screen,
                           (255-special_color[0], 255-special_color[1], 255 - special_color[2]),
                           special_block.center, 
                           radius=10
                            )

    for unbreakable_color, unbreakable_block in unbreakable_list:
        pygame.draw.rect(screen, unbreakable_color, unbreakable_block)
        pygame.draw.line(screen,
                         (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                         unbreakable_block.topleft,
                         unbreakable_block.bottomright,
                         width=3)
        
    #рисуем весло и мяч
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    

    #2 таймер скорости мяча и размера ракетки
    #скорость мяча со временем увеличивается, а ширина и высота ракетки уменьшаются
    timer1 += clock.get_rawtime() / 1000
    timer2 += clock.get_rawtime() / 1000
    change_ball_speed(change_period)
    change_paddle_size(change_period)
    

    #Движение мяча
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    

    #Столкновение слева
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Столкновение сверху
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #столкновение с веслом
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    

    #столкновение с блоками
    hitIndex = ball.collidelist(block_list)


    if hitIndex != -1:
        if block_list[hitIndex] not in unbreakable_block_list:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
        else:
            hitRect = block_list[hitIndex]
            hitColor = color_list[hitIndex]
        #если прямоугольник особенный, мы получаем за него 2 очка и проигрываем другой звук

        if hitRect in special_block_list:
            special_block_list.remove(hitRect)
            special_color_list.remove(hitColor)
            special_list.remove((hitColor, hitRect))
            game_score += 2
            special_collision_sound.play()
        #если прямоугольник попадания неразрывный, то не удаляем его ниоткуда и играем другой звук - vine Boom
        elif hitRect in unbreakable_block_list:
            boom_collision_sound.play()
        else:
            game_score += 1
            collision_sound.play()

        dx, dy = detect_collision(dx, dy, ball, hitRect)
      
        


    
    #счет игры
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #экран выигрыша и экран проигрыша 
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif all(block in unbreakable_block_list for block in block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    

    #контроль весла
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    #эта настройка — мое решение проблемы, когда мяч застревает в каком-то замкнутом контуре и продолжает двигаться только внутри него. По сути, нажав CTRL-H, пользователь может получить единоразовую помощь — снова поместить мяч в центр, но ценой +2 скорости.
    if (key[pygame.K_LCTRL] or key[pygame.K_RCTRL]) and key[pygame.K_h] and not help_used:
        ball.x = W // 2
        ball.y = H // 2
        ballSpeed += 2
        help_used = True
        

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()