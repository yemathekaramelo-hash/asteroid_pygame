import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # extra info
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # initializes the game
    pygame.init()

    # defines the clock
    clock = pygame.time.Clock()
    
    # defines deltatime
    dt = 0

    # sets screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    # initializes the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    # main game loop
    while True:
        log_state()

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # allows player movement
        updatable.update(dt)

        # checks collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()
            
        # adds the background
        screen.fill("black")

        # spawns the player
        for drawables in drawable:
            drawables.draw(screen)
        
        # refreshes the screen    
        pygame.display.flip()

        # limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000

# only start game if directly ran
if __name__ == "__main__":
    main()
