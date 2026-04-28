import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    # initializes the game
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # sets screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # initializes the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, 0)

    # main game loop
    while True:
        log_state()

        # adds the background
        screen.fill("black")

        # spawns the player
        player.draw(screen)
        
        # limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000
 
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()

            

if __name__ == "__main__":
    main()
