import pygame as pg
pg.init()

pg.image.load("Colours.png")

screen = pg.display.set_mode((800, 600))
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        player.draw(screen)
        pg.display.update()