import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked the x to close the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update everything
    pygame.display.update()
    clock.tick(60)
    













pygame.quit()          