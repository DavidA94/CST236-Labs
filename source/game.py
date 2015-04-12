class Game(object):
    def __init__(self):
        self.playing = True

    def button_pressed(self, button):
        if button == 'x' or button == 'X':
            self.playing = False
