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
        self.path = [(13, 82), (269, 82), (269, 177), (449, 177), (449, 85), (640, 85), (640, 295), (463, 295), (463, 507), (649, 507), (649, 413), (824, 413), (824, 507), (1200, 507)]
        self.path_pos = 0
        self.move_count = 0
        self.axis = ""
        self.next_point = 1
        self.x1, self.y1, self.x2, self.y2 = 0,0,0,0

    def draw(self, win):
        """
        Draws the enemy and animates it with the images provided in files
        :param win: surface
        :return: None
        """
        pass

    def collide(self,x,y):
        """
        Returns if a bullet has hit an enemy
        :param x: Int
        :param y: Int
        :return: Boolean
        """
        pass

    def move(self):
        """
        Move enemy along the path by following a certain number of dots plotted on the map
        :return: None
        """
        #take the positions of the first point
        #if the next point doesnt exist, you have reached the end of the line and the enemies dissapear    off the screen

        if self.next_point == 1:
            if self.path_pos + 1 < len(self.path):
                self.x1,self.y1 = self.path[self.path_pos]
                self.x2,self.y2 = self.path[self.path_pos + 1]
                self.next_point = 0
            #else:
                #enemy_group.remove(self)


        
        direction_x = 0
        direction_y = 0


        if self.x1 - self.x2 == 0:
            self.axis = "Y"
        if self.y1 - self.y2 == 0:
            self.axis = "X"

        if self.axis == "X":
            if self.x1 - self.x2 > 0:
                direction_x = -1
            if self.x1 - self.x2 < 0:
                direction_x = 1
        if self.axis == "Y":
            if self.y1 - self.y2 > 0:
                direction_y = -1
            if self.y1 - self.y2 < 0:
                direction_y = 1



        if self.path_pos >= len(self.path):
            self.x2, self.y2 = (-100, 507)

        self.move_speed = 1

        if self.axis == "X":
            if self.x1-self.x2 != 0:
                self.x1 = self.x1 + (self.move_speed * direction_x)
                self.rect.x = self.x1
        if self.axis == "Y":
            if self.y1-self.y2 != 0:
                self.y1 = self.y1 + (self.move_speed * direction_y)
                self.rect.y = self.y1
        if (self.axis == "X" and self.x1 - self.x2 == 0) or (self.axis == "Y" and self.y1 - self.y2 == 0):
            self.next_point = 1
            self.path_pos += 1


        #move_x, move_y = (self.rect.x + change_c[0] * self.move_count, self.rect.y + change_c[1] * self.move_count)


    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
        else:
            return False

    def update(self):
        self.move()


