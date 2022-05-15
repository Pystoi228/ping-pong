from pygame import *
from random import *
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
fon = (200,225, 200)
window = display.set_mode((700, 500))
window.fill(fon)

clock = time.Clock()
FPS = 60



class Player(GameSprite):
    def apdate(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y += 10
        if keys_pressed[K_s]:
            self.rect.y -= 10

lost = 0
toto = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y == 450:
            self.rect.y = 0
            self.rect.x = randint(0, 600)
            self.speed = randint(1, 3)
            lost = lost + 1
hero = Player('rrr.jpg', 0, 0, 1, 60, 60)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero.apdate()
    hero.reset()

                


    


   
    display.update()
    clock.tick(FPS)



    
    