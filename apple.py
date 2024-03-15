import random
import pygame

GRAVITY = 0.1
class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, 300)
        self.y = 0
        self.color = (0, 162, 232)
        self.radius = 10
        self.velocity_y = 0
        self.acceleration_y = GRAVITY

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def fall(self):

        self.velocity_y += self.acceleration_y
        self.y += self.velocity_y

        # in case the apple falls out of the screen

        if self.y > self.screen.get_height(): 
            self.y = 0
            self.x = random.randint(0, self.screen.get_width())
            self.velocity_y = 0
