from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
    
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
    
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

ball = GameSprite("kisspng-tennis-balls-ball-game-sport-yellow-ball-5ae160cbbfe885.1095474415247198197861 (1).png",5, win_height - 100, 50, 50, 10)

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
racket1 = Player('rocket.png', 30, 200, 40, 500, 150)
racket2 = Player('rocket.png', 520, 200, 40, 500, 150)
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e. type == QUIT:
            game = False
    ball.update()
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)


