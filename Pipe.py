from Bird import *
import random
PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'pipe.png')))


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.UP_PIPE = PIPE
        self.DOWN_PIPE = pygame.transform.flip(PIPE, False, True)

        self.passed = False
        self.height = random.randrange(50, 450)
        self.top = self.height - self.DOWN_PIPE.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, window):
        window.blit(self.DOWN_PIPE, (self.x, self.top))
        window.blit(self.UP_PIPE, (self.x, self. bottom))

