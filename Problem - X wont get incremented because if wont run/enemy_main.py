import pygame
import random
import math
import csv,os

class Enemy(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()
        self.height = height
        self.width = width
        self.image = pygame.Surface([35, 35])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = 82
        self.rect.x = 13
        self.imgs = []
        self.animation = []
        self.health = 1
        self.path = [(13, 82), (269, 82), (269, 177), (449, 177), (449, 85), (640, 85), (640, 295), (463, 295), (463, 507), (649, 507), (649, 413), (824, 413), (824, 507), (824, -50)]
        self.path_pos = 0
        self.move_count = 0

    def draw(self, win):
        """
        Draws the enemy and animates it with the images provided in files
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

    def update(self):
        """
        Move enemy along the path by following a certain number of dots plotted on the map
        :return: None
        """
        #take the positions of the first point
        #if the next point doesnt exist, you have reached the end of the line and the enemies dissapear    off the screen


        next_point = 1
        if next_point == 1:
            x1,y1 = self.path[self.path_pos]
            x2,y2 = self.path[self.path_pos + 1]
            next_point = 0

        self.rect.x = x1
        self.rect.y = y1

        axis = ""
        direction_x = 0
        direction_y = 0


        if x1 - x2 == 0:
            axis = "Y"
        if y1 - y2 == 0:
            axis = "X"

        if axis == "X":
            if x1 - x2 > 0:
                direction_x = -1
            if x1 - x2 < 0:
                direction_x = 1
        if axis == "Y":
            if y1 - y2 > 0:
                direction_y = 1
            if y1 - y2 < 0:
                direction_y = -1



        if self.path_pos >= len(self.path):
            x2, y2 = (-100, 507)

        self.move_speed = 1

        if axis == "X":
            if x1-x2 != 0:
                x1 = x1 + (self.move_speed * direction_x)
        if axis == "Y":
            if y1-y2 != 0:
                y1 = y1 + (self.move_speed * direction_y)
        if (axis == "X" and x1 - x2 == 0) or (axis == "Y" and y1 - y2 == 0):
            next_point = 1
            self.path_pos += 1


        #move_x, move_y = (self.rect.x + change_c[0] * self.move_count, self.rect.y + change_c[1] * self.move_count)
        print(x1,y1)

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
        else:
            return False

    def move(self):
        self.move()
        pass

