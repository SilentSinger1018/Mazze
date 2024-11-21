import pygame
import config
from gamemanager import Gamemanager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
gamemanager = Gamemanager(screen)
level = 1
level_limit = 2
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    if gamemanager.update():
        #已经顺利通关
        level += 1
        if level > level_limit:
            running = False
        else:
            gamemanager = Gamemanager(screen, level)
        
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(config.FPS)  # limits FPS to 60

pygame.quit()