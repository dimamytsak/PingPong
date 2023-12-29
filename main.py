from pygame import*

class GameSpite(sprite.Sprite):
    def __init__(self, player_img, x, y, speed, width, height):
        super().__init__()
        self.img = transform.scale(image.load(player_img), (width, height))
        self.speed = speed
        self.rect = self.img.get_rect
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
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (mw_height - 80):
            self.rect.y += self.speed


fon = (0, 3, 8)
mw_with = 600
mw_height = 500
mw = display.set_mode((mw_with, mw_height))
mw.fill(fon)