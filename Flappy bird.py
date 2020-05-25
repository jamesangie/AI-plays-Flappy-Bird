import neat
import time
import random
from Pipe import *

pygame.init()

# size of the window
WIDTH = 500
HEIGHT = 800

# Loading images of the objects
# a bird has three images showing the different state of the bird's wings
BASE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'base.png')))
BG = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'bg.png')))


def draw_window(window, bird, pipe):
    window.blit(BG, (0, 0))
    bird.draw(window=window)

    pipe.draw(window=window)
    pygame.display.update()


def main():
    bird = Bird(200, 200)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pipe = Pipe(500)
    running = 1
    while running:
        clock.tick(30)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        bird.move()
        pipe.move()
        draw_window(window, bird, pipe)

        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()


main()
