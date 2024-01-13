import pygame
import os


class Floor:
    IMAGE_FLOOR = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'base.png')))
    SPEED = 5
    WIDTH = IMAGE_FLOOR.get_width()

    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = self.WIDTH

    def move(self):
        self.x0 -= self.SPEED
        self.x1 -= self.SPEED

        if self.x0 + self.WIDTH <= 0:
            self.x0 = 0
            self.x1 = self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMAGE_FLOOR, (self.x0, self.y))
        screen.blit(self.IMAGE_FLOOR, (self.x1, self.y))
