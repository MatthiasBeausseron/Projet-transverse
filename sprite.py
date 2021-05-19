import pygame


# import sprite
# class blabla(sprite.MySprite)
# super().init("mummy")


class MySprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.images = pygame.image.load(f'photos/sprite/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
        self.time = 0

    def start_animation(self):
        self.animation = True

    def animate(self, mod, yes=False):
        if self.animation:
            self.current_image += 1
            self.time += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if yes is False:
                    self.animation = False
            if self.time%9 == 0:
                if mod == "SL":
                    self.image = self.images[self.current_image%4]
                if mod == "SR":
                    self.image = self.images[self.current_image%4 +5]
                if mod == "R":
                    self.image = self.images[self.current_image%4 + 10]
                if mod == "L":
                    self.image = self.images[self.current_image%4 + 15]
            if mod == "J":
                if self.time%15 == 0:
                    self.image = self.images[self.current_image%5 + 20]


def load_animation_images(sprite_name, length):
    images = []
    path = f"photos/sprite/{sprite_name}"

    for num in range(length):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        images[num] = pygame.transform.scale(images[num], (80, 150))
    return images


animations = {
    'Servietsky': load_animation_images('Servietsky', 26),
}