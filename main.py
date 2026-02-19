import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot


def main():
    # initialize pygame
    pygame.init()

    # setup pygame variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set up shots
    Shot.containers = (updatable, drawable, shots)

    # set up asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    # set up asteroid field
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # create player
    Player.containers = (updatable, drawable)
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
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()  # draw output to screen
        dt = clock.tick(60) / 1000  # advance delta time


if __name__ == "__main__":
    main()
