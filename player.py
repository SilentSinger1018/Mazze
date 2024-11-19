import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, center_x=config.SCREEN_WIDTH / 2, center_y=config.SCREEN_HEIGHT / 2):
        super().__init__()
        self.width = 100
        self.height = 50
        self.image_source = pygame.image.load("static/images/car.png").convert()
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)
        self.last_time = pygame.time.get_ticks()
        self.delta_time = 0
        self.move_velocity = 0

    def update_delta_time(self):
        current_time = pygame.time.get_ticks()
        self.delta_time = (current_time - self.last_time) / 1000
        self.last_time = current_time

    def input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self

    def move(self):
        vx = self.move_velocity * self.delta_time
        self.rect.x += vx

    def update(self):
        self.update_delta_time()
        self.move()

