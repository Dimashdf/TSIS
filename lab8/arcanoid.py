import pygame#импортируем pygame
import random# импортируем библиотеку рандом 

pygame.init()#инициализируем  pygame

W, H = 1200, 800#даем значение высоты и ширины
FPS = 40#даем значение фпс


screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)#создаем окно 
clock = pygame.time.Clock()#создаем обьект часов
done = False#даем  значения для done false чтобы использывать в будущем
bg = (0, 0, 0)#а это чтобы цвет был черным и дляизпользывание в будущем

# здесь мы создаем весло 
paddleW = 150#пишем  ширину для весло 
paddleH = 25#пишем высоту для весло
paddleSpeed = 20#пишем  скорость 
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)#тут уже создаем прямоугольник и располежим его  снизу экрана с небольшим отступом 

# Ball
ballRadius = 20#пишем радиус мячика 
ballSpeed = 6#пишем скорость
ball_rect = int(ballRadius * 2 ** 0.5)# Это переменная, которая определяет размер квадратного мяча
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)#тут уже создаем мячик и распаложим его по середине 
dx, dy = 1, -1#даем значение по оси х и по оси у

# счетчик 
game_score = 0#создаем счетчик и даем значение 0 
game_score_fonts = pygame.font.SysFont('comicsansms', 40)#
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))#создаем изобрежения текста с текстом your game score
game_score_rect = game_score_text.get_rect()#Получает прямоугольник, описывающий размеры и положение изображения текста.
game_score_rect.center = (210, 20)# Устанавливает центральную точку прямоугольника текста

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')#загружаем музыку

def detect_collision(dx, dy, ball, rect):#здесь создаем функцию чтобы дать направления мячу когда оно сталкивается с веслом
    if dx > 0:#Проверяет направление движения мяча по оси X. Если мяч движется вправо, вычисляется расстояние (delta_x) между правой стороной мяча и левой стороной прямоугольника.
        delta_x = ball.right - rect.left#
    else:# Если мяч движется влево, вычисляется расстояние (delta_x) между правой стороной прямоугольника и левой стороной мяча.
        delta_x = rect.right - ball.left
    if dy > 0:#Проверяет направление движения мяча по оси Y. Если мяч движется вниз, вычисляется расстояние (delta_y) между нижней стороной мяча и верхней стороной прямоугольника.
        delta_y = ball.bottom - rect.top
    else:#Если мяч движется вверх, вычисляется расстояние (delta_y) между нижней стороной прямоугольника и верхней стороной мяча.
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:#если это будеть меньше 10 пикселеи то это нам даст обнаружить столкновения
        dx, dy = -dx, -dy#Если столкновение произошло под углом, направление движения мяча меняется на противоположное по осям X и Y.
    if delta_x > delta_y:# Если delta_x больше delta_y, это означает, что столкновение произошло с боковой стороной прямоугольника. В этом случае меняется направление движения по оси Y.
        dy = -dy
    elif delta_y > delta_x:#Если delta_y больше delta_x, это означает, что столкновение произошло с верхней или нижней стороной прямоугольника. В этом случае меняется направление движения по оси X.
        dx = -dx
    return dx, dy# Возвращает новые значения dx и dy, которые учитывают столкновение мяча с прямоугольником.

# Block settings
unbreakable_block_list = [pygame.Rect(10 + 120 * i, 50, 100, 50) for i in range(10)]# создаем Список неразрушимых кирпичей. Каждый элемент списка - это прямоугольник
breakable_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(1, 4)]#создаем Список разрушимых кирпичей. Каждый элемент списка - это прямоугольник
unbreakable_color = (100, 100, 100)#даем неразрушымову серый цвет
breakable_color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(10 * 3)]#даем рандомные цвета для разрушимых кирпичей

# Speed up settings
speed_up_interval = 5000  # Увеличивать скорость каждые 5 секунд (в миллисекундах)
speed_up_amount = 1  # Увеличивать скорость на 1 единицу
last_speed_up_time = pygame.time.get_ticks()  # Время последнего увеличения скорости

# Decrease paddle settings
decrease_interval = 10000  # Уменьшать размер платформы каждые 10 секунд
decrease_amount = 10  # Уменьшать размер платформы на 10 пикселей
last_decrease_time = pygame.time.get_ticks()  # Время последнего уменьшения платформы

# Bonus brick settings
bonus_brick_list = [pygame.Rect(10 + 120 * i, 250, 100, 50) for i in range(10)]#создаем бонусных кирпичей 
bonus_brick_color = (255, 255, 0)  # Цвет бонусного кирпича
bonus_active = False  # Признак активного бонуса
bonus_duration = 5000  # Продолжительность бонуса в миллисекундах
bonus_start_time = 0  # Время начала бонуса
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

while not done:#до не равно done 
    for event in pygame.event.get():#
        if event.type == pygame.QUIT:#
            done = True#

    screen.fill(bg)#даем экрану черный цвет

    [pygame.draw.rect(screen, unbreakable_color, block) for block in unbreakable_block_list]#рисует все неразрушимые кирпичи в списке 
    [pygame.draw.rect(screen, breakable_color_list[idx], block) for idx, block in enumerate(breakable_block_list)]#рисует все разрушимые кирпичи в списке

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)#рисует платформу (paddle) белым цветом
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)#рисует мяч (ball) красным цветом.

    ball.x += ballSpeed * dx#обновляет позицию мяча на экране на основе его скорости и направления движения .
    ball.y += ballSpeed * dy#

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:#Этот код проверяет столкновения мяча с границами экрана и с платформой 
        dx = -dx#
    if ball.centery < ballRadius + 50:#
        dy = -dy#
    if ball.colliderect(paddle) and dy > 0:#
        dx, dy = detect_collision(dx, dy, ball, paddle)#

    hit_index = ball.collidelist(breakable_block_list)#
    if hit_index != -1:#
        hit_rect = breakable_block_list.pop(hit_index)#
        breakable_color_list.pop(hit_index)#
        dx, dy = detect_collision(dx, dy, ball, hit_rect)#
        game_score += 1#
        collision_sound.play()#
        if random.random() < 0.1 and not bonus_active:  # Вероятность появления бонусного кирпича
            bonus_active = True#
            bonus_start_time = pygame.time.get_ticks()#
        elif bonus_active and pygame.time.get_ticks() - bonus_start_time > bonus_duration:#
            bonus_active = False#
            paddleW += 100  # Увеличиваем ширину платформы на 15 пикселей

    if bonus_active:#
        bonus_brick_color = (255, 255, 255)  # Белый цвет для бонусных кирпичей
        [pygame.draw.rect(screen, bonus_brick_color, block) for block in bonus_brick_list]#
    else:#
        [pygame.draw.rect(screen, unbreakable_color, block) for block in bonus_brick_list]#

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))#
    screen.blit(game_score_text, game_score_rect)#

    if ball.bottom > H:#
        screen.fill((0, 0, 0))#
        screen.blit(losetext, losetextRect)#
    elif not len(breakable_block_list):#
        screen.fill((255, 255, 255))#
        screen.blit(wintext, wintextRect)#

    key = pygame.key.get_pressed()#
    if key[pygame.K_LEFT] and paddle.left > 0:#
        paddle.left -= paddleSpeed#
    if key[pygame.K_RIGHT] and paddle.right < W:#
        paddle.right += paddleSpeed#

    # Speed up ball
    current_time = pygame.time.get_ticks()#
    if current_time - last_speed_up_time > speed_up_interval:#
        ballSpeed += speed_up_amount#
        last_speed_up_time = current_time#

    # Decrease paddle size
    if current_time - last_decrease_time > decrease_interval and paddleW > 0:#
        paddleW -= decrease_amount#
        paddleW = max(paddleW, 0)  # Ensure paddle width doesn't go negative
        paddle.left += decrease_amount // 2  # Move paddle left to keep it centered
        paddle.width = paddleW#
        last_decrease_time = current_time#

    pygame.display.flip()#
    clock.tick(FPS)#