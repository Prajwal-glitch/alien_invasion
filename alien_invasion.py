import sys
import pygame
from settings import Settings

def run_game():
    #start game and create a window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #set background color
    bg_color = (230,230,230)

    #start the loop
    while True:

        #look for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #redraw screen
        screen.fill(settings.bg_color)
       
       #make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
