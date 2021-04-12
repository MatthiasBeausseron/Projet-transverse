import pygame

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('images/IdleD0.png'))
        self.images.append(pygame.image.load('images/IdleD1.png'))
        self.images.append(pygame.image.load('images/IdleD2.png'))
        self.images.append(pygame.image.load('images/IdleD4.png'))
        self.images.append(pygame.image.load('images/IdleD4.png'))
        self.images.append(pygame.image.load('images/IdleG0.png'))
        self.images.append(pygame.image.load('images/IdleG1.png'))
        self.images.append(pygame.image.load('images/IdleG2.png'))
        self.images.append(pygame.image.load('images/IdleG3.png'))
        self.images.append(pygame.image.load('images/IdleG4.png'))
         self.images.append(pygame.image.load('images/WalkServiet00.png'))
        self.images.append(pygame.image.load('images/WalkServiet01.png'))
        self.images.append(pygame.image.load('images/WalkServiet02.png'))
        self.images.append(pygame.image.load('images/WalkServiet03.png'))
        self.images.append(pygame.image.load('images/WalkServiet04.png'))
        self.images.append(pygame.image.load('images/WalkServiet05.png'))
        self.images.append(pygame.image.load('images/WalkServiet06.png'))
        self.images.append(pygame.image.load('images/WalkServiet07.png'))
        self.images.append(pygame.image.load('images/WalkServiet08.png'))
        self.images.append(pygame.image.load('images/WalkServiet09.png'))

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
