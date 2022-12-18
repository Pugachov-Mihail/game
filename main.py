import pygame
from models import Player, mobs
from config import WIDTH, HEIGHT, BLACK, FPS, ALL_SPRITES, MOBS, BULLETS

run_game = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player.Player()


def event_game():
    global run_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


def init_game():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Тест")


def running_game():
    screen.fill(BLACK)
    ALL_SPRITES.add(player)
    clock.tick(FPS)
    ALL_SPRITES.update()
    ALL_SPRITES.draw(screen)
    pygame.display.flip()


def main(mob):
    init_game()
    running_game()
    attac_player(mob)
    shots_player()
    event_game()


def create_more_mobs():
    for i in range(10):
        mob = mobs.Mod()
        ALL_SPRITES.add(mob)
        MOBS.add(mob)
    return MOBS


def shots_player():
    ALL_SPRITES.update()
    hits = pygame.sprite.groupcollide(MOBS, BULLETS, True, True)
    for hit in hits:
        m = mobs.Mod()
        ALL_SPRITES.add(m)
        MOBS.add(m)


def attac_player(MOBS):
    global run_game
    hits = pygame.sprite.spritecollide(player, MOBS, False)
    if hits:
        run_game = False


if __name__ == '__main__':
    mob_value = create_more_mobs()
    while run_game:
        main(mob_value)
