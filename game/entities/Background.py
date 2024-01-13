import pygame
import os


class Background:
    IMAGE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'bg.png')))
    SPEED = 1
    WIDTH = IMAGE_BACKGROUND.get_width()

    def __init__(self):
        self.y = 0
        self.x0 = 0
        self.x1 = self.WIDTH

    def move(self):
        self.x0 -= self.SPEED
        self.x1 -= self.SPEED

        if self.x0 + self.WIDTH <= 0:
            self.x0 = 0
            self.x1 = self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMAGE_BACKGROUND, (self.x0, self.y))
        screen.blit(self.IMAGE_BACKGROUND, (self.x1, self.y))
