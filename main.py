import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Pygame groups of updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Group for asteroid object
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # Group for shots object
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    # AsteroidField static container
    AsteroidField.containers = (updatable,)

    player_starting_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player = Player(player_starting_pos, shots)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Init black screen
        screen.fill((0, 0, 0))

        # Calculate dt in seconds and limit fps to 60
        dt = clock.tick(60) / 1000

        # Update all updatables
        for item in updatable:
            item.update(dt)

        # Draw all drawables
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
