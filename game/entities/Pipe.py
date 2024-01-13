import pygame
import os
import random


class Pipe:
    IMAGE_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'pipe.png')))
    DISTANCE = 200
    SPEED = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.pos_top = 0
        self.pos_bottom = 0
        self.pipe_top = pygame.transform.flip(self.IMAGE_PIPE, False, True)
        self.pipe_bottom = self.IMAGE_PIPE
        self.passed = False
        self.define_height()

    def define_height(self):
        self.height = random.randrange(50, 500)
        self.pos_top = self.height - self.pipe_top.get_height()
        self.pos_bottom = self.height + self.DISTANCE

    def move(self):
        self.x -= self.SPEED

    def draw(self, screen):
        screen.blit(self.pipe_top, (self.x, self.pos_top))
        screen.blit(self.pipe_bottom, (self.x, self.pos_bottom))

    def collide(self, bird):
        mask_bird = bird.get_mask()
        mask_top = pygame.mask.from_surface(self.pipe_top)
        mask_bottom = pygame.mask.from_surface(self.pipe_bottom)

        distance_top = (self.x - bird.x, self.pos_top - round(bird.y))
        distance_bottom = (self.x - bird.x, self.pos_bottom - round(bird.y))

        point_top = mask_bird.overlap(mask_top, distance_top)
        point_bottom = mask_bird.overlap(mask_bottom, distance_bottom)

        if point_top or point_bottom:
            return True

        return False
