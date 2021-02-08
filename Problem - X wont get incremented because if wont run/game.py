import pygame
import random
import math
import csv,os
from Enemies import enemy_main
# Define some colors

all_sprites_group = pygame.sprite.Group()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (150, 150, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Baloons TD")

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 1100
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.velocity = 4
        self.bg = pygame.image.load(os.path.join("images", "background.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
    def run(self):
        run = True
        enemy = enemy_main.Enemy(YELLOW, 10, 10)
        all_sprites_group.add(enemy)
        i = 0
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            all_sprites_group.update()

            self.win.blit(self.bg, (0, 0))
            all_sprites_group.draw(screen)
            pygame.display.flip()
        pygame.quit()


g = Game()
g.run()