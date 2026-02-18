import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    # initialize pygame
    pygame.init()

    # setup pygame variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # print game start message
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # gameloop
    while True:
        log_state()  # log gamestate to jsonl file
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit when user hits the quit button on pygame window
                return

        screen.fill("black")
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()  # draw output to screen
        dt = clock.tick(60) / 1000  # advance delta time


if __name__ == "__main__":
    main()
