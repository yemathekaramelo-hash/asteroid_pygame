import pygame
from constants import LINE_WIDTH

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):

        if hasattr(self,"containers"):
            super().__init__(self.containers)
        
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius 

    # to be overriden
    def draw(self, screen):
        pass

    # to be overidden
    def update(self, dt):
        pass

    