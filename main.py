from pygame import*

class GameSpite(sprite.Sprite):
    def __init__(self, player_img, x, y, speed, width, height):
        super().__init__()
        self.img = transform.scale(image.load(player_img), (width, height))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSpite):
    def right_player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (mw_height - 80):
            self.rect.y += self.speed
    def left_player(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (mw_height - 80):
            self.rect.y += self.speed

fon = (50, 3, 8)
mw_with = 600
mw_height = 500
mw = display.set_mode((mw_with, mw_height))
mw.fill(fon)

game = True
finish = False

clock = time.Clock()

fps = 60

raketka1 = Player('racket.png', 30, 200, 4, 50, 150)
raketka2 = Player('racket.png', 520, 200, 4, 50, 150)

ball = GameSpite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()

font = font.Font(None, 35)

lose1 = font.render('1 player Lose!', True, (188, 0, 0))
lose2 = font.render('2 player Lose!', True, (188, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mw.fill(fon)
        raketka1.left_player()
        raketka2.right_player()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(raketka1, ball) or sprite.collide_rect(raketka2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > mw_height - 50 or ball.rect.y < 0:
            speed_y *= - 1
        if ball.rect.x < 0:
            finish = True
            mw.blit(lose1, (200, 200))
            game_over = True
        if ball.rect.x > mw_with:
            finish = True
            mw.blit(lose2, (200, 200))
            game_over = True
        raketka1.reset()
        raketka2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)
