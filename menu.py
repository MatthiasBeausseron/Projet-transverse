import pygame

class Menu():
    def __init__(self, game):
        pygame.mixer.init()
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 40, 40)
        self.offset = - 100


    def draw_cursor(self):
        self.game.draw_text('×', 60, self.cursor_rect.x, self.cursor_rect.y-5)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def music(self, song):
        choice = pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 80
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 120
        self.bonusx, self.bonusy = self.mid_w, self.mid_h + 160
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 200
        self.quitx, self.quity = self.mid_w, self.mid_h + 240
        self.cursor_rect.midtop = (self.startx + self.offset-34, self.starty)
        self.music("photos/Main_Theme_Brawl.mp3")

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.YELLOW)
            self.game.image()
            self.game.draw_text("Main Menu", 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 45, self.startx, self.starty)
            self.game.draw_text("Options", 40, self.optionsx, self.optionsy)
            self.game.draw_text("Bonus", 35, self.bonusx, self.bonusy)
            self.game.draw_text("Credits", 29, self.creditsx, self.creditsy)
            self.game.draw_text("Quit", 30, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset+20, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.bonusx + self.offset+43, self.bonusy)
                self.state = "Bonus"
            elif self.state == "Bonus":
                self.cursor_rect.midtop = (self.creditsx + self.offset+48, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.quitx + self.offset+68, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.startx + self.offset-34, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.quitx + self.offset+68, self.quity)
                self.state = "Quit"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset-34, self.starty)
                self.state = "Start"
            elif self.state == "Bonus":
                self.cursor_rect.midtop = (self.optionsx + self.offset+20, self.optionsy)
                self.state = "Options"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.creditsx + self.offset+48, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.bonusx + self.offset+43, self.bonusy)
                self.state = "Bonus"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Bonus':
                self.game.curr_menu =self.game.bonus
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.quit

            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 40
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.volx + self.offset+30, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((self.game.YELLOW))
            self.game.image()
            self.game.draw_text('Options',100 , self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 40, self.volx, self.voly)
            self.game.draw_text("Controls", 40, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.controlsx + self.offset+10, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.volx + self.offset+25, self.voly)
                self.state = 'Volume'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.controls
        self.run_display = False

class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volupx, self.volupy = self.mid_w + 75, self.mid_h + 50
        self.voldownx, self.voldowny = self.mid_w + -80, self.mid_h + 10
        self.cursor_rect.midtop = (self.volupx + self.offset, self.volupy)
        self.sound = pygame.mixer.music.set_volume(0.5)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.YELLOW)
            self.game.image()
            self.game.draw_text('Volume', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("+", 90, self.volupx, self.volupy)
            self.game.draw_text("_", 110, self.voldownx, self.voldowny)
            self.game.draw_text("*Press Left*", 15, self.game.DISPLAY_W/ 2 - 82, self.game.DISPLAY_H / 2 +100)
            self.game.draw_text("*Press Right*", 15, self.game.DISPLAY_W/ 2 + 78, self.game.DISPLAY_H / 2 +100)
            self.draw_volume()
            self.blit_screen()

    def move_cursor(self):
        if self.game.RIGHT_KEY :
            if self.state == '+':
                self.state = '+'
                self.cursor_rect.midtop = (self.volupx + self.offset, self.volupy)
            elif self.state == '-':
                self.state = '-'
                self.cursor_rect.midtop = (self.voldownx + self.offset, self.voldowny)

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.LEFT_KEY:
            self.volume = pygame.mixer.music.get_volume() - 0.09
            pygame.mixer.music.set_volume(self.volume)
        elif self.game.RIGHT_KEY:
            self.volume = pygame.mixer.music.get_volume() + 0.09
            pygame.mixer.music.set_volume(self.volume)
        elif self.game.LEFT_KEY and 0.000 < pygame.mixer.music.get_volume() <0.1000 :
            pygame.mixer.music.set_volume(0)
        self.run_display = False

    def draw_volume(self):
        if pygame.mixer.music.get_volume() == 0.0:
            self.game.draw_text("-|X               |+", 60, self.game.DISPLAY_W/2 -22, self.game.DISPLAY_H/2 +200)
        elif 0.0 < pygame.mixer.music.get_volume() <= 0.1:
            self.game.draw_text("-|◙               |+", 60, self.game.DISPLAY_W/2 -22, self.game.DISPLAY_H/2 +200)
        elif 0.1 <pygame.mixer.music.get_volume() <= 0.2:
            self.game.draw_text("-|◙◙              |+", 60, self.game.DISPLAY_W/2 -18, self.game.DISPLAY_H/2 +200)
        elif 0.2 < pygame.mixer.music.get_volume() <= 0.3:
            self.game.draw_text("-|◙◙◙            |+", 60, self.game.DISPLAY_W / 2 - 18, self.game.DISPLAY_H / 2 + 200)
        elif 0.3 <pygame.mixer.music.get_volume() <= 0.4:
            self.game.draw_text("-|◙◙◙◙          |+", 60, self.game.DISPLAY_W / 2 - 18, self.game.DISPLAY_H / 2 + 200)
        elif 0.4 < pygame.mixer.music.get_volume() <= 0.5:
            self.game.draw_text("-|◙◙◙◙◙         |+", 60, self.game.DISPLAY_W / 2 - 18, self.game.DISPLAY_H / 2 + 200)
        elif 0.5 <pygame.mixer.music.get_volume() <= 0.6:
            self.game.draw_text("-|◙◙◙◙◙◙       |+", 60, self.game.DISPLAY_W / 2 - 22, self.game.DISPLAY_H / 2 + 200)
        elif 0.6 < pygame.mixer.music.get_volume() <= 0.7:
            self.game.draw_text("-|◙◙◙◙◙◙◙     |+", 60, self.game.DISPLAY_W / 2 - 22, self.game.DISPLAY_H / 2 + 200)
        elif 0.7 < pygame.mixer.music.get_volume() <= 0.8:
            self.game.draw_text("-|◙◙◙◙◙◙◙◙    |+", 60, self.game.DISPLAY_W / 2 - 22, self.game.DISPLAY_H / 2 + 200)
        elif 0.8 < pygame.mixer.music.get_volume() <= 0.9:
            self.game.draw_text("-|◙◙◙◙◙◙◙◙◙  |+", 60, self.game.DISPLAY_W / 2 - 22, self.game.DISPLAY_H / 2 + 200)
        elif 0.9 < pygame.mixer.music.get_volume() < 1:
            self.game.draw_text("-|◙◙◙◙◙◙◙◙◙◙ |+", 60, self.game.DISPLAY_W / 2 - 22, self.game.DISPLAY_H / 2 + 200)
        elif pygame.mixer.music.get_volume() == 1:
            self.game.draw_text("-|◙◙◙◙◙◙◙◙◙◙◙|+", 60, self.game.DISPLAY_W / 2 - 22, self.game.DISPLAY_H / 2 + 200)


class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.YELLOW)
            self.game.image()
            self.game.draw_text('Controls',100 , self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Player 1', 40, self.game.DISPLAY_W/ 2 -200, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Press "left_arrow" to go left', 30, self.game.DISPLAY_W/ 2 -200, self.game.DISPLAY_H / 2 + 90)
            self.game.draw_text('Press "right_arrow" to go right', 30, self.game.DISPLAY_W/ 2 -200, self.game.DISPLAY_H / 2 + 130)
            self.game.draw_text('Press "up_arrow" to jump', 30, self.game.DISPLAY_W/ 2 -200, self.game.DISPLAY_H / 2 + 170)
            self.game.draw_text('Press "M" to attack', 30, self.game.DISPLAY_W/ 2 -200, self.game.DISPLAY_H / 2 + 210)
            self.game.draw_text('Press "L" to grab', 30, self.game.DISPLAY_W / 2 -200, self.game.DISPLAY_H / 2 + 250)
            self.game.draw_text('Player 2', 40, self.game.DISPLAY_W / 2+200, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Press "Q" to go left', 30, self.game.DISPLAY_W / 2 +200, self.game.DISPLAY_H / 2 + 90)
            self.game.draw_text('Press "D" to go right', 30, self.game.DISPLAY_W / 2 +200, self.game.DISPLAY_H / 2 + 130)
            self.game.draw_text('Press "Z" to jump', 30, self.game.DISPLAY_W / 2 +200, self.game.DISPLAY_H / 2 + 170)
            self.game.draw_text('Press "F" to attack', 30, self.game.DISPLAY_W / 2 + 200, self.game.DISPLAY_H / 2 + 210)
            self.game.draw_text('Press "G" to grab', 30, self.game.DISPLAY_W / 2 + 200, self.game.DISPLAY_H / 2 + 250)
            self.blit_screen()

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.YELLOW)
            self.game.image()
            self.game.draw_text('Credits',100 , self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Matthias BEAUSSERON', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Jean DOUTRIAUX', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 90)
            self.game.draw_text('Quentin FOURIE', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 130)
            self.game.draw_text('Victor JULOU', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 170)
            self.game.draw_text('ROMAIN PLOT', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 210)
            self.blit_screen()

class BonusMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Coop'
        self.coopx, self.coopy = self.mid_w, self.mid_h + 30
        self.cursor_rect.midtop = (self.coopx + self.offset+40, self.coopy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((self.game.YELLOW))
            self.game.image()
            self.game.draw_text('Bonus', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text("Coop", 40, self.coopx, self.coopy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
                pass#ajouter la boucle du jeu bonus

class QuitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.YELLOW)
            self.game.image()
            self.game.draw_text('Thanks for playing! See you soon...',65 , self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('®', 30, self.game.DISPLAY_W / 2 + 395, self.game.DISPLAY_H / 2 +350)
            self.game.draw_text('All rights reserved', 20,self.game.DISPLAY_W / 2 + 500, self.game.DISPLAY_H / 2 + 350)
            self.blit_screen()
            pygame.time.wait(5000)
            self.run_display = False
            pygame.quit()