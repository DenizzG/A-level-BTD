import pygame
import random
import math
import csv,os

# Define some colors

all_sprites_group = pygame.sprite.Group()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 100, 255)
GREY1 = (230,230,230)
GREY2 = (190,190,190)
GREY3 = (150,150,150)
GREY4 = (120,120,120)
GREY5 = (100,100,100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (150, 150, 255)
YELLOW = (255, 255, 0)

pygame.init()

size = (1300, 700)
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background = background.convert()
pygame.display.set_caption("Baloons TD")


class Game(pygame.sprite.Sprite):
    def __init__(self):
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
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:




            self.draw()


        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        pygame.display.update()

all_sprites_group.update()
# --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image

screen.fill(BLACK)

    # --- Drawing code should go here
g = Game()
g.run()
all_sprites_group.draw(screen)


# --- Go ahead and update the screen with what we've drawn.
pygame.display.flip()


# Close the window and quit.
pygame.quit()
