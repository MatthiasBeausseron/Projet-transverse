import pygame


# import sprite
# class blabla(sprite.MySprite)
# super().init("mummy")


class MySprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()

        self.images = pygame.image.load(f'images/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

        def start_animation():
            self.animation = True

        def animate(self, yes=False):
            self.current_image += 1

            if self.current_image >= len(self.images):
                self.current_image = 0
                if yes is False:
                    self.animation = False

            self.image = self.images[self.current_image]


def load_animation_images(sprite_name):
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"

    for num in range(1, 24):
        image_path = images + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    return images


animations = {
    'IdleD': load_animation_images('IdleD')
    'IdleG': load_animation_images('IdleG')
    'WalkServietD' : load_animation_images('WalkServietD')
    'walkServietG' : load_animation_images('WalkServietG')
}