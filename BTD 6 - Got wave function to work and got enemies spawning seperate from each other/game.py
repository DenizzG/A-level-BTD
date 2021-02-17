import pygame
import random
import math
import csv,os
from Enemies import enemy_main
# Define some colors

all_sprites_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

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
        self.wave_n = 10
        self.enemy_cooldown = 1
        self.enemy_spawn_timer = 0

    #Every round,after all enemmimes have died the next wave starts. Each wave the game must get ahrder and harder
    def wave(self):
        while self.wave_n != 0 and self.enemy_cooldown == 1:
            self.enemy_spawn_timer = pygame.time.get_ticks()
            self.wave_n = self.wave_n - 1
            enemy = enemy_main.Enemy(YELLOW, 10,10)
            all_sprites_group.add(enemy)
            enemy_group.add(enemy)
            self.enemy_cooldown = 0

    def run(self):
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.wave()
            if pygame.time.get_ticks() - self.enemy_spawn_timer > 150:
                self.enemy_cooldown = 1

            all_sprites_group.update()

            self.win.blit(self.bg, (0, 0))
            all_sprites_group.draw(screen)
            pygame.display.flip()
        pygame.quit()


g = Game()
g.run()