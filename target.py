import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 60
        self.height = 60
        self.image_source = pygame.image.load("static/images/target.png").convert()
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.up_size = 1.1
        self.low_size = 0.9
        self.size = 1
        self.size_rate = 0.01

    def update(self):
        self.size += self.size_rate
        if(self.size >= self.up_size or self.size <= self.low_size):
            self.size_rate = -self.size_rate
        self.image = pygame.transform.scale(self.image_source, (self.width * self.size, self.height * self.size))
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center    