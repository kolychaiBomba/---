from pygame import *

#todo окно
window = display.set_mode((1000, 700))
display.set_caption('Пинг-понг')

background = transform.scale(image.load('fon.png'), (1000, 700))

clock = time.Clock()
FPS = 70

#mixer.init()
#mixer.music.load('alarming.mp3')
#mixer.music.play()

font.init()
font1 = font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 36)
#print(font.get_fonts())

#! класс игрока
class qwerSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.rotate( transform.scale(image.load(player_image), (160, 160)), 295)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 5    
        if keys_pressed[K_d] and self.rect.x < 950:
            self.rect.x += 5
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y < 600: 
            self.rect.y += 5   
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5    
        if keys_pressed[K_RIGHT] and self.rect.x < 950:
            self.rect.x += 5
        if keys_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_UP] and self.rect.y < 600:
            self.rect.y += 5

#? класс мячика
class boll(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.rotate( transform.scale(image.load(player_image), (170, 110)), 0)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.x += self.speed
        global lost
        if self.rect.x > 1000:
            self.rect.y = randint(0,  300)
            lost += 1
            self.rect.x = 0

game = True
finish = True



while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish: 
        pass
    else:
        text_win = font2.render('Победил 1 игрок!!!', 1, (230, 191, 0))
        window.blit(text_win,(400, 300))
        text_win2 = font2.render('Победил 2 игрок!!!', 1, (230, 191, 0))
        window.blit(text_win,(400, 300))
    display.update()
    clock.tick(FPS)