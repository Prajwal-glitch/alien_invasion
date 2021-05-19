class Settings():
    """ A class to store all settings for Alien invasion"""

    def __init__(self):
        """Intiliaze the game's settingss."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed_factor = 1.5
