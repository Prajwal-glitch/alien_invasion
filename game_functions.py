import sys

import pygame

def check_events():
    """respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(setting, screen, ship):
    #redraw the screen during each pass through loop.
    screen.fill(setting.bg_color)
    ship.blitme()

    #make the most recent drawn screen visible
    pygame.display.flip()
