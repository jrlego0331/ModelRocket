import pygame
import sys
import os
from time import sleep
from math import sin, cos, radians, atan

#initialize
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0,0)
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

#screen settings
screenWidth = 1920
ScreenHeight = 1080
floorY = ScreenHeight/5*3.5
pygame.display.set_caption("Cannonball")
screen = pygame.display.set_mode((screenWidth, ScreenHeight))

#FPS settings
clock = pygame.time.Clock()
FPS = 60

#Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0,255, 0)


cannonBallPos = []
r = 30
cannonBallPos.append((r+4, floorY-r - 1))

g = 9.8 * 0.01

check = False

while not check:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            xpos, ypos = pygame.mouse.get_pos()
            xpos+=int(r/2)
            angle = atan((cannonBallPos[0][1] - ypos) / (xpos - cannonBallPos[0][0]))
            v0 = ((cannonBallPos[0][1] - ypos)**2 + (xpos - cannonBallPos[0][0])**2)**0.5 / 80
            screen.fill(Black)
            check = True
    
    screen.fill(Black)
    pygame.draw.rect(screen, White, (0, floorY, screenWidth, ScreenHeight-floorY))
    pygame.draw.line(screen, (220, 220, 50), (cannonBallPos[0][0], cannonBallPos[0][1]), pygame.mouse.get_pos(), 4)
    pygame.display.update()

def drawCannonball(t):
    for pos in cannonBallPos:
        col = 50 + t
        if col > 255: col = 255
        pygame.draw.circle(screen, (255- col, 255, 255-col), pos, r)

def calculateCannonball(t):
    for n in range(len(cannonBallPos)):
        xpos, ypos = cannonBallPos[n]
        deltaX = v0 * cos(angle)
        deltaY = v0 * sin(angle) - g*t
        pos = (xpos+deltaX, ypos-deltaY)
        cannonBallPos[n] = pos


frame = 0

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    calculateCannonball(frame)
    
    if cannonBallPos[-1][1] > floorY - r: break


    pygame.draw.rect(screen, White, (0, floorY, screenWidth, ScreenHeight-floorY))
    drawCannonball(frame)
    pygame.display.update()
    frame +=1

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit(0)