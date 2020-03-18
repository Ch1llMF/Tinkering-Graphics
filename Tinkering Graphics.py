import pygame as pg
pg.init()

Red = (237, 28, 36)
Green = (34, 177, 76)
Blue = (63, 72, 204)
Yellow = (255, 242, 0)
Orange = (255, 127, 39)

def colourSwap(surf, from_, to_):
    arr = pg.PixelArray(surf)
    arr.replace(Red, Blue)
    del arr

pg.image.load("Colours.png")

screen = pg.display.set_mode((800, 600))
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        player.draw(screen)
        pg.display.update()