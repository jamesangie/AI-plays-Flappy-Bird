import pygame

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(imgs/bird1.png)), pygame.transform.scale2x(pygame.image.load(imgs/bird2.png)), pygame.transform.scale2x(pygame.image.load(imgs/bird3.png))]


# defining bird object.
class Bird:
    # Loading default variables of a Bird
    IMG = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    # initializing a Bird. with initial coordinate (x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # tilting the bird because that's what the game does. Bird is flat
        self.tilt = 0
        # count tick to show different states of wings and different angles of tilting
        self.tick_count = 0
        # velocity of the bird
        self.vel = 0
        # We need a height even though we have y because when we tilt the bird the image should be drawn at different
        # height
        self.height = self.y
        # count image so that we know which one we need to draw
        self.img_count = 0
        # image of the bird with states
        self.img = self.IMG[0]

    # jump function so that the bird can fly up and jump
    def jump(self):
        # vel is negative because negative is upward in a window
        self.vel = -10.5
        # track when is this jump happening
        self.tick_count = 0
        # where is the bird starting from
        self.height = self.y

    # function that moves the bird which we will call every frame(tick)
    def move(self):
        self.tick_count += 1
        # basically a physics formula that sets the gravity drag down the bird and fly up the bird when we have a jump
        vertical_move = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        # set vertical_move to 16 if it is higher than 16 so that the bird is not flying to high too quick
        if vertical_move >= 16:
            vertical_move = 16
        # let the jump higher to make the jump nicer. remember negative is upward
        elif vertical_move < 0:
            vertical_move -= 2

        self.y = self.y + d
        # check if the bird is higher than the jump position or lower to make the tilting
        # tilt up when the bird is higher than the jump position, tilt down otherwise
        # it is confusing but that was the what original game like
        if vertical_move < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    # function that display the bird on the window
    def draw(self, window):
        # Count the image to use different
        self.img_count += 1
        # check what image we need to show.
        # the bird does not move its wings if we are going down so:
        if self.tilt <= -80:
            self.img = self.IMG[0]
            self.img_count = 0
        else:
            if self.img_count < self.ANIMATION_TIME:
                self.img = self.IMG[0]
            elif self.img_count < self.ANIMATION_TIME * 2:
                self.img = self.Img[1]
            elif self.img_count < self.ANIMATION_TIME * 3:
                self.img = self.Img[2]
            elif self.img_count < self.ANIMATION_TIME * 4:
                self.img = self.Img[0]
                self.img_count = 0
        # Pygame only allows rotations from the top left conner but that will be really weird
        # so we need this lines of magical code to let the bird rotating from the center
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_furface(self.img)