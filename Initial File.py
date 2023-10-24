import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400)) # (width, height)
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('C:/Users\kalco\Coding Projects\Python\Pygame-Test\\font\Pixeltype.ttf', 50) # (font type, font size)

sky_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\Sky.png')
ground_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\ground.png')
text_surface = test_font.render('My Game', False, 'Black') # (text, Anti-Aliasing, color)

snail_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\snail\snail1.png')
snail_x_pos = 600

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked the x to close the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))  
    screen.blit(text_surface, (300, 50))  
    snail_x_pos -= 1
    if snail_x_pos < -100: 
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250)) 
            
    # update everything
    pygame.display.update()
    clock.tick(60)
    


# This closes the game window once the while-loop above ends when the x button is pressed
pygame.quit()          