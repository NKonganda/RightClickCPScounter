import pygame
from sys import exit
black = (0, 0, 0)
white = (255, 255, 255)
count = 0
pygame.font.init()
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('cps: ', False, (0, 0, 0))
running = True
screen = pygame.display.set_mode((320, 200))
pygame.display.set_caption('right click cps counter')
screen.blit(textsurface,(0,0))
fps = 60
fps_clock = pygame.time.Clock()
start_time = 0
passed_time = 0
array = [0]*60
clickps = 0


def cps():
    global clickps
    clickps = 0
    for i in range(len(array)-1, len(array)-60, -1):
        clickps += array[i]


while running:
    array.append(0)
    cps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if start_time == 0:
                    start_time = pygame.time.get_ticks()
                if passed_time > 0:
                    array.append(1)


    if start_time != 0:
        passed_time = (pygame.time.get_ticks() - start_time) / 1000

    clicks_surface = myfont.render('Clicks: {}'.format(clickps), True, black)

    screen.fill(white)
    screen.blit(clicks_surface, (30, 70))
    pygame.display.flip()
    fps_clock.tick(fps)
