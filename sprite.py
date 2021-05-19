import pygame

"""
This class is used to create sprites for the character of the game.
We have a dictionary that create an array of all the images of the character used in animation. 
The dictionary allows to not create a new array each time the class is called.
It is created by the function "load" that create the array in function of the name of the character.  
Then we use the function "animate" to play the different animations of the character in function
of their movements. 
The function "start_animation" allows to have "animation" which are only activated when an action is performed, allowing other animations to be played non-stop. 

"""
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
                if mod == "CL":
                    self.image = self.images[self.current_image%8]
                if mod == "CR":
                    self.image = self.images[self.current_image%8 + 26]
                if mod == "NR":
                    self.image = self.images[self.current_image%6 + 46]
                if mod == "NL":
                    self.image = self.images[self.current_image%6 + 20]
            if mod == "JR":
                if self.time%4 == 0:
                    self.image = self.images[self.current_image%6 + 27]
            if mod == "JL":
                if self.time%4 == 0:
                    self.image = self.images[self.current_image%7 + 20]
            if mod == "CJR":
                if self.time%4 == 0:
                    self.image = self.images[self.current_image%12 + 34]
            if mod == "CJL":
                if self.time%4 == 0:
                    self.image = self.images[self.current_image%12 + 8]


def load_animation_images(sprite_name, length):
    images = []
    path = f"photos/sprite/{sprite_name}"

    for num in range(length):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        images[num] = pygame.transform.scale(images[num], (80, 150))
    return images


animations = {
    'Servietsky': load_animation_images('Servietsky', 33),
    'Celest' : load_animation_images('Celest', 51)
}
