import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400)) # (width, height)
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
running = True

test_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\Sky.png')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked the x to close the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(test_surface, (0,0))     
            
    # update everything
    pygame.display.update()
    clock.tick(60)
    




# This closes the game window once the while-loop above ends when the x button is pressed
pygame.quit()          