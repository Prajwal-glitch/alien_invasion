import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
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
        gf.check_events()
        gf.update_screen(setting,screen,iship)        

run_game()
