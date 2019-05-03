import pygame
from pygame.locals import *  # noqa
import sys
import random


class Game:

    def __init__(self):
        #screen
        self.screenw = 400
        self.screenh = 708
        self.screen = pygame.display.set_mode((self.screenw, self.screenh))
        pygame.display.set_caption("flappy gay")
        #coordinates
        self.birdX = 60
        self.birdY = 50

        #b00lshit
        self.jump = 0
        self.dead = False

        #useful
        self.gravity = 5
        self.jumpSpeed = 104

        #wall things
        self.wallX = 400
        self.offset = random.randint(10, 568)
        self.gap = 130

        #
        self.counter = 0

    def wallsUpdate(self):
        self.wallX -= 2
        if self.wallX < -80:
            self.wallX = 400
            self.counter += 1
            self.offset = random.randint(10, 568)

    def birdUpdate(self):
        if self.jump:
            #jump things
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            #gravity lul
            self.birdY += self.gravity
            self.gravity += 0.2

        #rect coordinates
        if ((self.birdX + 30 >= self.wallX and self.birdX + 30 <= self.wallX + 80) or (self.birdX >= self.wallX and self.birdX <= self.wallX + 80)) and ((self.birdY <= self.offset or self.birdY >= self.offset + self.gap) or (self.birdY + 25 <= self.offset or self.birdY + 25 >= self.offset + self.gap)):
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(10, 568)
            self.gravity = 5
            self.wallX = 400

        if not 0 < self.birdY < self.screenh+25:
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(10, 568)
            self.gravity = 5
            self.wallX = 400


    def show(self):
        #before mainloop
        clock = pygame.time.Clock()
        #font lul
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        #mainloop
        while True:
            #60 fps
            clock.tick(60)
            #all events
            for event in pygame.event.get():
                #esc = concede
                if event.type == pygame.QUIT:
                    sys.exit()
                #if jump
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 10

            #fucking background
            self.screen.fill((0, 0, 0))
            #draw wall lul
            pygame.draw.rect(self.screen, (220,220,220), (self.wallX, self.offset, 80, -self.offset))
            pygame.draw.rect(self.screen, (220,220,220), (self.wallX, self.offset+self.gap, 80, self.screenh-self.offset-self.gap))
            #draw ma bird (ball)
            pygame.draw.rect(self.screen, (255, 255, 255), (self.birdX, self.birdY, 30, 25))
            #score
            self.screen.blit(font.render(str(self.counter), False, (255, 0, 0)), (200,60))
            #im so stupid
            self.wallsUpdate()
            self.birdUpdate()
            pygame.display.update()


#lets go dude
if __name__ == "__main__":
    Game().show()
