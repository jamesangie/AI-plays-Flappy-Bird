from Pipe import *

BASE = pygame.transform.scale2x(pygame.image.load(os.path.join(image_path, 'base.png')))


class Base:
    WIDTH = BASE.get_width()
    IMG = BASE

    def __init__(self):
        self.y = 700
        self.x_first = 0
        self.x_second = self.x_first + self.WIDTH

    def move(self):
        self.x_first -= 5
        self.x_second -= 5
        # when the first image is off screen, remove it and let the second image become the first
        # then create a new second image
        if self.x_first < -self.WIDTH:
            self.x_first = self.x_second
            self.x_second = self.x_first + self.WIDTH

    def draw(self, window):
        window.blit(self.IMG, (self.x_first, self.y))
        window.blit(self.IMG, (self.x_second, self.y))

