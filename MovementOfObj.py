import pygame
import sys
from matplotlib import pyplot as plt
import os
from time import sleep

#initialize
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (1000,45)
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

#screen settings
screenWidth = 460
ScreenHeight = 800
pygame.display.set_caption("Movement of Object")
screen = pygame.display.set_mode((screenWidth, ScreenHeight))

#FPS settings
clock = pygame.time.Clock()
FPS = 60

#Colors
Black = (0, 0, 0)
White = (255, 255, 255)

#given info
t = 0
v0 = 40
g = -10
startPos = int(ScreenHeight/4*3+20)

#object positioning
obj_position = []
obj_position.append((screenWidth/2, startPos))

s_log = []
s_log.append(0)
v_log = []
v_log.append(v0)
t_log = []
t_log.append(t)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            print('\n   Chart\n---------------------')
            for n in range(len(obj_position)):
                print('|',n, 'th: ', obj_position[n][1], 'px')
            print('---------------------')

            t = 0
            obj_position = []
            obj_position.append((screenWidth/2, startPos))

            s_log = []
            s_log.append(0)
            v_log = []
            v_log.append(v0)
            t_log = []
            t_log.append(t)
            plt.subplot(1, 2, 1)
            plt.clf()
            plt.subplot(1, 2, 2)
            plt.clf()

    # next position calculation
    new_position = obj_position[-1][1] - v0*t - 0.5*g*t**2
    obj_position.append((screenWidth/2, new_position))
    
    #velocity calculation
    v = v0 + g*t

    #detail printing
    fontObj = pygame.font.SysFont('arial.ttf', 17)
    textLine = '   t = '+ str(int(t)) + 's  v = ' + str(v) + 'px/s  v0 = 30px/s'
    textSurfaceObj = fontObj.render(textLine, True, Black, White)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 16)

    textSurfaceObj2 = fontObj.render('Click HERE to reset', True, Black, White)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (350, 60)

    textPos = fontObj.render(str(startPos - obj_position[-1][1]) + 'px', True, Black, White)
    textRectPos = textSurfaceObj2.get_rect()
    textRectPos.center = (screenWidth/2+150, obj_position[-1][1])

    #graphics
    screen.fill(White)
    pygame.draw.line(screen, (255, 0, 0), (0, startPos), (screenWidth, startPos), 4)
    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj2, textRectObj2)
    screen.blit(textPos, textRectPos)
    for n in range(len(obj_position)):
        obj_col = 255 - int(255/len(obj_position)) * n
        pygame.draw.circle(screen, (obj_col, obj_col, 255), obj_position[n], 20)
        pygame.draw.circle(screen, (obj_col, 255, obj_col), obj_position[n], 20, 2)
    pygame.display.update()
    t+=1
    
    #Graphing
    s_log.append(int(startPos - obj_position[-1][1]))
    v_log.append(v)
    t_log.append(t)

    plt.rcParams["figure.figsize"] = (10,5)
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.grid'] = True
    
    plt.subplot(1, 2, 1)
    plt.plot(t_log, v_log, color='green')
    plt.title('V - T', fontsize=20)
    plt.xlabel('Time(s)', fontsize=10)
    plt.ylabel('Velocity(px/s)', fontsize=10)
    plt.ylim([-300, 50])

    plt.subplot(1, 2, 2)
    plt.plot(t_log, s_log, color='blue')
    plt.title('S - T', fontsize=20)
    plt.xlabel('Time(s)', fontsize=10)
    plt.ylabel('Displacement(px)', fontsize=10)
    plt.ylim([-500, 250])
    
    plt.pause(0.01)