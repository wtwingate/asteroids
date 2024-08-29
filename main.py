import pygame

from constants import *
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    delta_time = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(delta_time)

        screen.fill(color=(0, 0, 0))
        player.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
