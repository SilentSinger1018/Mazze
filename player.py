import pygame
import config
import math

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
        self.move_acc = 600 #加速度
        self.move_velocity = 0 #当前的移动速度
        self.move_velocity_limit = 220 #移动速度的上限
        self.smallest_rotate_move = 30 #使得车子可以克服摩擦力转动的最小角速度
        self.rotate_velocity = 0 
        self.rotate_velocity_limit = 140 #角速度移动上限
        self.forward_angle = 0 #车身与水平线的角度
        self.friction = 0.9

    def update_delta_time(self):
        current_time = pygame.time.get_ticks()
        self.delta_time = (current_time - self.last_time) / 1000
        self.last_time = current_time

    def input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.move_velocity += self.move_acc * self.delta_time
            self.move_velocity = min(self.move_velocity, self.move_velocity_limit)
        elif key_pressed[pygame.K_DOWN]:
            self.move_velocity -= self.move_acc * self.delta_time
            self.move_velocity = max(self.move_velocity, -self.move_velocity_limit)
        else:
            self.move_velocity = self.move_velocity * self.friction

        sign = 1
        if(self.move_velocity < 0):
            sign = -1

        if key_pressed[pygame.K_RIGHT]:
            self.rotate_velocity = sign * self.rotate_velocity_limit
        elif key_pressed[pygame.K_LEFT]:
            self.rotate_velocity = -sign * self.rotate_velocity_limit
        else:
            self.rotate_velocity = 0
                
    def rotate(self, direction = 1):
        self.forward_angle += self.rotate_velocity * self.delta_time * direction
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)
        self.image.set_colorkey("black")
        #需要按照中心点旋转，所以旋转前后的中心点不会发生变化
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self, direction = 1):
        if(abs(self.move_velocity) > self.smallest_rotate_move):
            self.rotate(direction)
        vx = self.move_velocity * math.cos(math.pi * self.forward_angle / 180) * direction
        vy = self.move_velocity * math.sin(math.pi * self.forward_angle / 180) * direction
        self.rect.x += vx * self.delta_time 
        self.rect.y += vy * self.delta_time

    def crash(self):
        self.move(-1)
        if(self.move_velocity > 0):
            self.move_velocity = max(-100, -self.move_velocity)
        else:
            self.move_velocity = min(100, -self.move_velocity)

    def update(self):
        self.update_delta_time()
        self.input()
        self.move()