import pygame
import random
from config import RED, WIDTH, HEIGHT


class Mod(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, 40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.speedy = random.randrange(1, 8)