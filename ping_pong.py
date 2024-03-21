from pygame import*
class GameSprite(sprite.Sprite):
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width-80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width-80:
            self.rect.y += self.speed



   
bg = (200, 255, 255)
win_height = 500
win_width = 600
win = display.set_mode((win_width, win_height))
win.fill(bg)

game = True
clock = time.Clock()
FPS = 60

mirko = Player("racket.png",30,200,4,50,150)
svirko = Player("racket.png",520,200,4,50,150)
dirko = GameSprite("tenis_ball.png",200,200,4,50,50)

font.init()
font = font.Font(None,35)
lose1 = font.render("PLAYER 1 LOSES", True, (180,0,0))
lose2 = font.render("PLAYER 2 LOSES", True, (180,0,0))




finish = False

speed_x = 3
speed_y = 3


while game:
    for a in event.get():
        if a.type == QUIT:
            game = False
    if finish != True:
        win.fill(bg)
        dirko.rect.x += speed_x
        dirko.rect.y += speed_y
        mirko.reset()
        svirko.reset()
        dirko.reset()
        mirko.update_l()
        svirko.update_r()
    if dirko.rect.y > win_height-50 or dirko.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(mirko,dirko) or sprite.collide_rect(svirko,dirko):
        speed_x *= -1
        speed_y *= 1
    if dirko.rect.x < 0:
        finish = True
        win.blit(lose1,(200,200))
        game = True

    if dirko.rect.x < 0:
        finish = True
        win.blit(lose2,(200,200))
        game = True

    display.update()
    clock.tick(FPS)