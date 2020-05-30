import neat
import time
from Base import *

pygame.init()

# size of the window
WIDTH = 500
HEIGHT = 800

# Loading images of the objects
# a bird has three images showing the different state of the bird's wings
BG = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'bg.png')))


# The function that we draw the bird and the pipe on the window
def draw_window(window, bird, pipe, base):
    window.blit(BG, (0, 0))
    bird.draw(window=window)
    pipe.draw(window=window)
    base.draw(window=window)
    pygame.display.update()


def main():
    bird = Bird(200, 200)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    base = Base()
    pipe = [Pipe(500)]
    running = 1
    # there is only one necessary pipe at one time. which is the pipe on the screen
    # we use a integer to access this pipe in the pipe list
    pipe_count = 0
    # count the score
    score = 0
    while running:
        clock.tick(30)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        bird.move()
        pipe[pipe_count].move()
        base.move()
        draw_window(window, bird, pipe[pipe_count], base)

        # show the lose state when the bird collides with any pipe
        if pipe[pipe_count].collision(bird) or bird.y > 700:
            print("lose")

        # increment score when the bird pass a pipe. Need to round pipe.x because difference
        # between real time and the frame in the game
        if pipe[pipe_count].x // 5 * 5 == 200:
            score += 1
            print(score)
        # Add a new pipe when the last one is off the screen
        if pipe[pipe_count].x == -80:
            pipe += [Pipe(500)]
            pipe_count += 1
        # jump the bird when click (that is how we play BABE!)
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()


main()
