class Settings():
    """All setting in the game"""
    def __init__(self):
        """Initialize's the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (66, 134, 244)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
