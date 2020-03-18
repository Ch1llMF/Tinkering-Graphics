import pygame as pg
pg.init()

Red = (237, 28, 36)
Green = (34, 177, 76)
Blue = (63, 72, 204)         # Colours that you can choose from
Yellow = (255, 242, 0)
Orange = (255, 127, 39)


def colourSwap(surf):
    arr = pg.PixelArray(surf)  # Change FROM to the colour you want to change from the image
    arr.replace(FROM, TO)   # Change TO to the colour you want to change the colour to
    del arr

# This should open the image called Colours then copy it.
# After copying it colourSwap will run where the colour will be changed.
class image:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.image.load('Colours.png').convert()
        self.rect = self.image.get_rect(center=self.screen_rect.center)
        colourSwap(self.image)

# This is the code that will actually draw the colour changed image so it can be shown in a pygame window.
    def draw(self, surf):
        surf.blit(self.image, self.rect)

# This script will open a window using pygame which will show the newly edited image.
screen = pg.display.set_mode((1920, 1080))
screen_rect = screen.get_rect()
player = image(screen_rect)
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        player.draw(screen)
        pg.display.update()