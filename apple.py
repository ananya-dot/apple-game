import random
import pygame
import math

GRAVITY = 0.1
class Apple:
    def __init__(self, screen, color):
        self.screen = screen
        self.x = random.randint(0, 300)
        self.y = 0
        self.color = color
        self.radius = 10
        self.velocity_y = 0
        self.acceleration_y = GRAVITY

        if self.color == 'red':
            self.image = pygame.transform.scale(pygame.image.load('assets/Diamond.png'), (70, 50))
        elif self.color == 'black':
            self.image = pygame.transform.scale(pygame.image.load('assets/asteroid.png'), (50, 50))
    def draw(self):
        # self.color = random.choice(["red", "black"])
        self.screen.blit(self.image, (self.x, self.y))
        # pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def fall(self):

        self.velocity_y += self.acceleration_y
        self.y += self.velocity_y

        # in case the apple falls out of the screen

        if self.y > self.screen.get_height(): 
            self.y = 0
            self.x = random.randint(0, self.screen.get_width())
            self.velocity_y = 0
