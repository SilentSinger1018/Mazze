import pygame 

class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 50
        self.height = 50
        self.image_source = pygame.image.load("static\images\star.png").convert()
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
