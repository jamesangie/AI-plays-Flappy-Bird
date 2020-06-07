import neat
import time
from Base import *
import pickle

pygame.init()

# size of the window
WIDTH = 500
HEIGHT = 800

# Loading images of the objects
# a bird has three images showing the different state of the bird's wings
BG = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'bg.png')))


# The function that we draw the bird and the pipe on the window
def draw_window(window, birds, pipe, base):
    window.blit(BG, (0, 0))
    for bird in birds:
        bird.draw(window=window)
    pipe.draw(window=window)
    base.draw(window=window)
    pygame.display.update()


def main(genomes, config):

    # the network
    nets = []
    # the set of genomes
    ge = []
    # the list of birds
    birds = []

    # by accessing genomes in Neat module, we can create each bird for each genome, we can keep track of the fitness of
    # each bird and we can then create the training progress
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets += [net]
        birds += [Bird(200, 200)]
        g.fitness = 0
        ge += [g]

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    base = Base()
    pipes = [Pipe(500)]
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

        pipes[pipe_count].move()
        base.move()
        draw_window(window, birds, pipes[pipe_count], base)

        # end the generation if no birds left
        if len(birds) == 0:
            running = False
            break

        # moves for each bird each frame
        for i, bird in enumerate(birds):
            bird.move()
            # reward when the bird move(live for one more frame)
            ge[i].fitness += 0.1
            # activate the neural network using the output of how far the bird is from the gap for next pipe
            output = nets[i].activate((bird.y, abs(bird.y - pipes[pipe_count].height),
                                       abs(bird.y - pipes[pipe_count].bottom)))
            if output[0] > 0.5:
                bird.jump()

            # remove the bird, the genome from the network and give punishments when the bird collides with any pipe or
            # off the screen
            if pipes[pipe_count].collision(bird) or bird.y > 700 or bird.y < 0:
                ge[i].fitness -= 1
                birds.pop(i)
                nets.pop(i)
                ge.pop(i)

        # increment score when the bird pass a pipe. Need to round pipe.x because difference
        # between real time and the frame in the game
        if pipes[pipe_count].x // 5 * 5 == 200:
            score += 1
            # reward the birds that pass a pipe
            for g in ge:
                g.fitness += 5
            print(score)
        # Add a new pipe when the last one is off the screen
        if pipes[pipe_count].x == -80:
            pipes += [Pipe(500)]
            pipe_count += 1

        if score > 30:
            running = 0
            break

        # jump the bird when click (that is how we play BABE!)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        # bird.jump()


def run(configpath):
    # set up Neat with default values defined in config-feedforward.txt
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                configpath)
    # setting the population
    p = neat.Population(config)
    # getting the output
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)


if __name__ == "__main__":
    """open up configuration for NEAT and run the training"""
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
