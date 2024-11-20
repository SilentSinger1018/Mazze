import pygame
from player import Player
from wall import Wall
from star import Star
from collided import collided_rect

class Gamemanager:
    def __init__(self, screen, level = 1):
        self.player = Player(200, 400)
        self.walls = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.level = level
        self.screen = screen
        self.load()
    
    def load_wall(self, walls):
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)

    def load_star(self, stars):
        for x, y in stars:
            star = Star(x, y)
            star.add(self.stars)

    def load(self):
        with open("static/maps/level%d.txt" % self.level, 'r') as fin:
            walls_cnt = int(fin.readline())
            walls = []
            for i in range(walls_cnt):
                wall = map(int, fin.readline().split())
                walls.append(wall)
            self.load_wall(walls)

            stars_cnt = int(fin.readline())
            stars = []
            for i in range(stars_cnt):
                star = map(int, fin.readline().split())
                stars.append(star)
            self.load_star(stars)
            

    def collide_detect(self):
        if pygame.sprite.spritecollide(self.player, self.walls, False, collided_rect):
            self.player.crash()

    def update(self):
        self.player.update()
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.draw(self.screen)
        self.stars.draw(self.screen)
        self.collide_detect()

