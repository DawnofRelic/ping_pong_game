from pygame import*

bg = (200, 255, 255)
win_height = 600
win_width = 500
win = display.set_mode((win_height, win_width))
win.fill(bg)

game = True
clock = time.Clock()
FPS = 60


while game:
    for a in event.get():
        if a.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)