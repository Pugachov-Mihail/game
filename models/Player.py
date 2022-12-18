import pygame
from config import GREEN, WIDTH, HEIGHT, ALL_SPRITES, BULLETS
from models.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedX = 0

    def update(self):
        self.speedX = 0
        keystate = pygame.key.get_pressed()
        self.press_key(keystate)
        self.display_player()
        self.rect.x += self.speedX

    def press_key(self, keystate):
        if keystate[pygame.K_LEFT]:
            self.speedX = -8
        if keystate[pygame.K_a]:
            self.speedX = -8
        if keystate[pygame.K_RIGHT]:
            self.speedX = 8
        if keystate[pygame.K_d]:
            self.speedX = 8

    def display_player(self):
        if self.rect.left > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        ALL_SPRITES.add(bullet)
        BULLETS.add(bullet)
