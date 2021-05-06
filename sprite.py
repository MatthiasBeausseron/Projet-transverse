import pygame


# import sprite
# class blabla(sprite.MySprite)
# super().init("mummy")


class MySprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.images = pygame.image.load(f'photos/assets/{sprite_name}/{sprite_name}.png')
        
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
        self.time = 0

    def start_animation():
        self.animation = True

    def animate(self, yes=False):
        self.current_image += 1
        self.time += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
            if not yes:
                self.animation = False
        if self.time%6 == 0:
            self.image = self.images[self.current_image]


def load_animation_images(sprite_name):
    images = []
    path = f"photos/assets/{sprite_name}/{sprite_name}"

    for num in range(0, 5):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        images[num] = pygame.transform.scale(images[num], (100, 150))
    return images


animations = {
    'IdleD': load_animation_images('IdleD'),
    'IdleG': load_animation_images('IdleG'),
    'WalkServietD' : load_animation_images('WalkServietD'),
    'walkServietG' : load_animation_images('WalkServietG')
}