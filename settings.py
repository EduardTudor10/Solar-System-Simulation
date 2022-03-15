import pygame

class Settings():
    """A class to store all the settings of the simulation"""

    def __init__(self):
        self.WIDTH = 700
        self.HEIGHT = 700
        self.CAPTION = "Solar System Simulation"
        self.BG = pygame.image.load("space background.jpg")
        self.BG = pygame.transform.scale(self.BG, (700, 700))

        # Colors
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 191, 255)
        self.RED = (220, 20, 60)
        self.GREY = (105, 105, 105)
        self.WHITE = (255, 255, 255)
        self.BROWN = (201, 144, 57)
        self.PINK = (206, 206, 206)
