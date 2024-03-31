import pygame

def drawRectangle(screen, start, end, color):
    pygame.draw.rect(screen, color, (start, (end[0]-start[0], end[1]-start[1])), 2)

def drawCircle(screen, center, radius, color):
    pygame.draw.circle(screen, color, center, radius, 2)

def erase(screen, position, radius):
    pygame.draw.circle(screen, (0, 0, 0), position, radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'pen'
    color = (255, 255, 255)
    points = []
    center = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'rectangle'
                if event.key == pygame.K_c:
                    mode = 'circle'
                if event.key == pygame.K_e:
                    mode = 'eraser'
                if event.key == pygame.K_1:
                    color = (255, 0, 0)  # Красный
                if event.key == pygame.K_2:
                    color = (0, 255, 0)  # Зеленый
                if event.key == pygame.K_3:
                    color = (0, 0, 255)  # Синий
                if event.key == pygame.K_4:
                    color = (0, 0, 0)  # Черный
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'rectangle':
                    start = pygame.mouse.get_pos()
                elif mode == 'circle':
                    center = pygame.mouse.get_pos()
                    radius = 0
                elif mode == 'eraser':
                    erase(screen, pygame.mouse.get_pos(), radius)
                points = []  # Обнуляем список точек
            if event.type == pygame.MOUSEMOTION:
                if mode == 'circle':
                    radius = max(radius, pygame.math.Vector2(center).distance_to(pygame.mouse.get_pos()))
                else:
                    points.append(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'rectangle':
                    end = pygame.mouse.get_pos()
                    drawRectangle(screen, start, end, color)
                elif mode == 'circle':
                    if center:
                        drawCircle(screen, center, radius, color)
                elif mode == 'eraser':
                    erase(screen, pygame.mouse.get_pos(), radius)
                points = []  # Обнуляем список точек
                center = None
                pygame.display.flip()  # Обновляем экран
        
        screen.fill((0, 0, 0))
        
        # Рисуем все точки, если это не ластик
        if mode != 'eraser':
            for i in range(len(points) - 1):
                pygame.draw.line(screen, color, points[i], points[i + 1], 2)
        
        pygame.display.flip()
        
        clock.tick(60)

main()