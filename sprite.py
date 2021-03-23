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

        self.index = 0

        self.cnt = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        if self.cnt % 9 == 0:
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.cnt += 1
