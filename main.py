import pygame

from constants import *


def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    delta_time = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))
        pygame.display.flip()

        elapsed_time = clock.tick(60)
        delta_time += elapsed_time / 1000


if __name__ == "__main__":
    main()
