import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400)) # (width, height)
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('C:/Users\kalco\Coding Projects\Python\Pygame-Test\\font\Pixeltype.ttf', 50) # (font type, font size)

sky_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\Sky.png').convert()
ground_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black') # (text, Anti-Aliasing, color)

snail_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))
# The 300 integer comes from the placement of the ground surface
player_surface = pygame.image.load('C:/Users\kalco\Coding Projects\Python\Pygame-Test\graphics\player\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
 
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked the x to close the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
            
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))  
    screen.blit(text_surface, (300, 50))  

    snail_rect.x -= 1
    if snail_rect.right <= 0:
        snail_rect.left = 800 # this is the size of the screen
    screen.blit(snail_surface, snail_rect) 
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)): # (x,y) mouse coordinate is determined by mouse.get_pos()
    #     print(pygame.mouse.get_pressed())
            
    # update everything
    pygame.display.update()
    clock.tick(60)
    


# This closes the game window once the while-loop above ends when the x button is pressed
pygame.quit()          