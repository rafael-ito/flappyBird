import pygame
import os


class Bird:
    IMGS = [
        pygame.transform.scale2x(pygame.image.load(os.path.join('img', f'bird{i}.png')))
        for i in range(1, 4)
    ]
    ROTATION_MAX = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = y
        self.time = 0
        self.count_image = 0
        self.image_index = 0
        self.image = self.IMGS[self.image_index]

    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        self.time += 1

        transition = 1.5 * (self.time**2) + self.speed * self.time
        if transition > 16:
            transition = 16
        elif transition < 0:
            transition -= 2
        self.y += transition

        if transition < 0 or self.y < (self.height + 50):
            if self.angle < self.ROTATION_MAX:
                self.angle = self.ROTATION_MAX
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def update_animation(self):
        self.count_image += 1
        if self.count_image % self.ANIMATION_TIME == 0:
            self.image_index = (self.image_index + 1) % len(self.IMGS)
            self.image = self.IMGS[self.image_index]

            if self.angle <= -80:
                # Special case: if angle is less than -80, set image to the second frame
                self.image = self.IMGS[1]

            self.count_image = 0

    def draw(self, screen):
        self.update_animation()

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        image_center_position = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_image.get_rect(center=image_center_position)

        screen.blit(rotated_image, rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
