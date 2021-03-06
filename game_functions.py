import sys

import pygame

def check_events(ship):
    """respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
def update_screen(setting, screen, ship):
    #redraw the screen during each pass through loop.
    screen.fill(setting.bg_color)
    ship.blitme()

    #make the most recent drawn screen visible
    pygame.display.flip()
