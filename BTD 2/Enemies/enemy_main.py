import pygame
import random
import math
import csv,os

class Enemy(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        self.height = height
        self.width = width
        self.image = pygame.Surface([35, 35])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.imgs = []
        self.animation = []
        self.health = 1
        self.path = [(13, 82), (269, 81), (275, 177), (449, 180), (452, 84), (640, 84), (638, 295), (463, 297), (461, 503), (649, 511), (650, 413), (824, 412), (827, 507)]
        self.path_pos = 0
        self.move_count = 0
        self.dis = 0

    def draw(self, win):
        """
        Draws the enemy and animates it with teh images provided in files
        :param win: surface
        :return: None
        """
        pass

    def collide(self,x1,y1):
        """
        Returns if a bullet has hit an enemy
        :param x: Int
        :param y: Int
        :return: Boolean
        """
        if x1 <= self.x + self.width and x1 >= self.x:
            if y1 <= self.y + self.height and y1 >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy along the path by folowing a certain number of dots plotted on the map
        :return: None
        """
        #take the positions of teh first point
        #if the next point doesnt exist, you have reached the end of the line and the enemies disapear    off teh screen
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 507)
        else:
            x2,y2 = self.path[self.path_pos + 1]

        distance = math.sqrt((x2-x1)**2 +(y2-y1)**2)

        self.move_count += 1
        change_c = (x2-x1, y2-y1)

        move_x, move_y = (self.x + change_c[0] * self.move_count, self.y + change_c[1] * self.move_count)
        self.dist += math.sqrt((x2-x1)**2 + (y2 -y1)**2)

        # go to the next point
        if self.dist >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
        self.x = move_x
        self.y = move_y


    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
        else:
            return False

    def update(self):
