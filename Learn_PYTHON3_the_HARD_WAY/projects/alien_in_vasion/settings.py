class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""

        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 30
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3