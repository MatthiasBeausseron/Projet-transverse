import pygame

class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('photos/sprite/IdleD0.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleD1.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleD2.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleD3.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleD4.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleG0.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleG1.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleG2.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleG3.png'))
        self.images.append(pygame.image.load('photos/sprite/IdleG4.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet00.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet01.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet02.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet03.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet04.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet05.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet06.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet07.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet08.png'))
        self.images.append(pygame.image.load('photos/sprite/WalkServiet09.png'))

        self.index = 0
        self.idle = 0
        self.cnt = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.cnt % 9 == 0:
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        if self.idle == 0:
            self.image = self.images[self.index % 5]

        if self.idle == 1:
            self.image = self.images[self.index % 5 + 5]

        if keys[pygame.K_RIGHT]:
            self.image = self.images[self.index % 5 + 10]
            self.idle = 0
        if keys[pygame.K_LEFT]:
            self.image = self.images[self.index % 5 + 15]
            self.idle = 1

        self.cnt += 1
