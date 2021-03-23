import pygame

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.imagesR = []
        self.imagesL = []
        self.imagesR.append(pygame.image.load('images/IdleD0.png'))
        self.imagesR.append(pygame.image.load('images/IdleD1.png'))
        self.imagesR.append(pygame.image.load('images/IdleD2.png'))
        self.imagesR.append(pygame.image.load('images/IdleD4.png'))
        self.imagesR.append(pygame.image.load('images/IdleD4.png'))
        self.imagesL.append(pygame.image.load('images/'))

        self.index = 0

        self.cnt = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def updateR(self):
        if self.cnt % 9 == 0:
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.cnt += 1
    

    def updateL(self):
        if self.cnt % 9 == 0:
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.cnt += 1
