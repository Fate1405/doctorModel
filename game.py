import pygame as pg
import sys

pg.init()
pg.font.init()
pg.mixer.init()

constants = {
    "width" : 800,
    "height" : 800,
    "fps" : 60
}

screen = pg.display.set_mode((constants["width"], constants["height"]))
clock = pg.time.Clock()

menuBackground = pg.image.load("./assets/waiting-room.jpg")
music = pg.mixer.music.load("./assets/music.mp3")
enterImage = pg.image.load("./assets/enter.jpeg")

def writeText(size, posx, posy, colour, text, surface, background):
    font = pg.font.Font("./assets/doctor.ttf", size)
    font_rect = font.render(text, True, colour, background)
    surface.blit(font_rect, (posx, posy))


class Button():
    def __init__(self, x, y, image, screen, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (width * scale, height * scale)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                return True

class GameState():
    def __init__(self):
        self.state = "intro"

    def intro(self):
        clock.tick(constants["fps"])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()

        screen.blit(menuBackground, (0, 0))
        writeText(50, constants["width"] / 2 - 325, constants["height"] / 8, (0, 0, 0), "Doctor Jaipal's (mal)practice", screen, (255, 255, 255))
        switch = startButton.draw()

        if switch:
            self.state = 'mainGame'

        pg.display.flip()
    
    def mainGame(self):
        clock.tick(constants["fps"])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()

        screen.blit(menuBackground, (0, 0))
        writeText(50, constants["width"] / 2 - 325, constants["height"] / 8, (0, 0, 0), "success", screen, (255, 255, 255))
        startButton.draw()

        pg.display.flip()

    def stateManager(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "mainGame":
            self.mainGame()
            

startButton = Button(constants["width"] / 3, constants["height"] * 0.75, enterImage, screen, 0.5)

def main():

    game = GameState()

    running = True

    pg.mixer.music.play(-1)

    while running:
        game.stateManager()

main()

pg.quit()