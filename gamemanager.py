import pygame
from player import Player
from wall import Wall
from star import Star
from target import Target
from collided import collided_rect, collided_circle

class Gamemanager:
    def __init__(self, screen, level = 1):
        self.player = None
        self.walls = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.level = level
        self.screen = screen
        self.stars_cnt = 0
        self.eat_cnt = 0
        self.load()
    
    def load_wall(self, walls):
        self.walls.empty()
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)

    def load_star(self, stars):
        self.stars.empty()
        for x, y in stars:
            star = Star(x, y)
            star.add(self.stars)

    def load_target(self, targets):
        self.targets.empty()
        for x, y in targets:
            target = Target(x, y)
            target.add(self.targets)

    def load(self):
        with open("static/maps/level%d.txt" % self.level, 'r') as fin:
            walls_cnt = int(fin.readline())
            walls = []
            for i in range(walls_cnt):
                wall = map(int, fin.readline().split())
                walls.append(wall)
            self.load_wall(walls)

            stars_cnt = int(fin.readline())
            self.stars_cnt = stars_cnt
            stars = []
            for i in range(stars_cnt):
                star = map(int, fin.readline().split())
                stars.append(star)
            self.load_star(stars)

            targets_cnt = int(fin.readline())
            targets = []
            for i in range(targets_cnt):
                target = map(int, fin.readline().split())
                targets.append(target)
            self.load_target(targets)

            x, y = map(int, fin.readline().split())
            self.player = Player(x, y)


    def collide_detect(self):
        if pygame.sprite.spritecollide(self.player, self.walls, False, collided_rect):
            self.player.crash()
        if pygame.sprite.spritecollide(self.player, self.stars, True, collided_circle):
            self.eat_cnt += 1
        if self.eat_cnt == self.stars_cnt and pygame.sprite.spritecollide(self.player, self.targets, True, collided_circle):
            return True
        return False
        

    def update(self):
        self.player.update()
        self.stars.update()
        self.targets.update()
        self.stars.draw(self.screen)
        self.walls.draw(self.screen)
        self.targets.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        return self.collide_detect()

