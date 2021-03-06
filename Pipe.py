from Bird import *
import random

PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'pipe.png')))


class Pipe:
    # GAP between up and down pipes
    GAP = 200
    # velocity of the pipe
    VEL = 5

    # Initialize a pipe object. The input x is the x coordinate of the pipe
    def __init__(self, x):
        self.x = x
        self.height = 0
        # We know that there are two pipes in Flappy Bird: one is upward one is downward
        self.top = 0
        self.bottom = 0
        self.UP_PIPE = PIPE
        self.DOWN_PIPE = pygame.transform.flip(PIPE, False, True)
        # the y coordinate of the pipe is randomized in range(50, 450)
        self.passed = False
        self.height = random.randrange(50, 450)
        self.top = self.height - self.DOWN_PIPE.get_height()
        self.bottom = self.height + self.GAP

    # function that we call each frame to move the pipe
    def move(self):
        self.x -= self.VEL

    # Draw pipe on the window
    def draw(self, window):
        window.blit(self.DOWN_PIPE, (self.x, self.top))
        window.blit(self.UP_PIPE, (self.x, self. bottom))

    # Calculate the collision of pipe and bird using mask method of pygame
    def collision(self, bird):
        bird_mask = bird.get_mask()
        up_mask = pygame.mask.from_surface(self.UP_PIPE)
        down_mask = pygame.mask.from_surface(self.DOWN_PIPE)

        down_offset = (self.x - bird.x, self.top - round(bird.y))
        up_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(up_mask, up_offset)
        t_point = bird_mask.overlap(down_mask, down_offset)

        if t_point or b_point:
            return True

        return False

