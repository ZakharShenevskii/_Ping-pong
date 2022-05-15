from pygame import *
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (size_x, size_y))
         self.rect = self.image.get_rect()
         self.rect.y = player_y
     def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN', True, (255, 255, 255))
lose = font1.render('YOU LOSE', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)

score = 0
window = display.set_mode((700, 500))
background = (170, 255, 150)
window.fill(background)

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

clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

  #if finish != True:

    clock.tick(FPS)
    display.update()