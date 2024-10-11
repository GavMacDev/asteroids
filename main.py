# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame


# import everything from constants.py
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        for p in updatable:
            p.update(dt)

        for a in asteroids:
            if a.collision(player):
                print(f"Game Over!")
                sys.exit()
            
            for shot in shots:
                if a.collision(shot):
                    shot.kill()
                    a.kill()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()  

        # limit the framerate to 60 FPS 
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
