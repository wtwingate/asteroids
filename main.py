import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    delta_time = 0

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))

        for item in updatable:
            item.update(delta_time)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
