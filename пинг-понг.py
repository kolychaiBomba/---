from pygame import *

#todo. окно
window = display.set_mode((1000, 700))
display.set_caption('Пинг-понг')

background = transform.scale(image.load('fon.png'), (1000, 700))

clock = time.Clock()
FPS = 70

#mixer.init()
#mixer.music.load('alarming.mp3')
#mixer.music.play()

font.init()
font2 = font.SysFont('tahoma', 50)
#print(font.get_fonts())

#! класс игрока
class qwerSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 200))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y < 500: 
            self.rect.y += 5   
    def update2(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += 5

RAKETKA = qwerSprite('raketka.png', 20, 300, 2)
RAKETKA2 = qwerSprite('raketka.png', 900, 300, 2)

#? класс мячика
class Ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (120, 120))
        self.speed_x = player_speed
        self.speed_y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        pass

RAKETKA = qwerSprite('raketka.png', 20, 300, 2)
RAKETKA2 = qwerSprite('raketka.png', 930, 300, 2)
BALL = Ball('boll.png', 50, 50, 5)

game = True
finish = True
q = 0
player1 = 0

while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
                game = False
    if finish: 
        if sprite.collide_rect(RAKETKA, BALL):
            if q == 0:
                q = 1
            if q >= 1:
                q += 1
            if q == 14:
                BALL.speed_x *= -1
                q = 0
        if sprite.collide_rect(RAKETKA2, BALL):
            if q == 0:
                q = 1
            if q >= 1:
                q += 1
            if q == 8:
                BALL.speed_x *= -1
                q = 0
        RAKETKA.update()
        RAKETKA2.update2()
        RAKETKA.reset()
        RAKETKA2.reset()
        BALL.rect.x += BALL.speed_x
        BALL.rect.y += BALL.speed_y
        if BALL.rect.y > 610 or BALL.rect.y < 0:
            BALL.speed_y *= -1
        BALL.update()
        BALL.reset()
        if BALL.rect.x > 950:
            finish = False
        if BALL.rect.x < 0:
            player1 = 1
            finish = False
    else:
        window.blit(background, (0, 0))
        if player1 == 1:
            text_win = font2.render('Победил 1 игрок!!!', 1, (255, 255, 255))
            window.blit(text_win,(400, 300))
        else:
            text_win2 = font2.render('Победил 2 игрок!!!', 1, (255, 255, 255))
            window.blit(text_win2,(300, 300))
    display.update()
    clock.tick(FPS)
