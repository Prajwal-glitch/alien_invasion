import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #start game and create a window
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    iship = Ship(screen)
    
    #set background color
    bg_color = (230,230,230)

    #start the loop
    while True:

        #look for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #redraw screen
        screen.fill(setting.bg_color)
        iship.blitme()
       #make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
