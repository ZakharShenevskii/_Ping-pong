from pygame import *
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (size_x, size_y))
         self.rect = self.image.get_rect()
         self.speed = player_speed
         self.rect.y = player_y
         self.rect.x = player_x
     def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))
font.init()
font1 = font.SysFont('Arial', 80)
lose1 = font1.render('player 1 lose!', True, (255, 255, 255))
lose2 = font1.render('player 2 lose!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)

score = 0
window = display.set_mode((700, 500))
background = (170, 255, 150)
window.fill(background), (win_width, win_height)
speed_x = 3
speed_y = 3
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

racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(background)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_height-50 or ball.rect.y > 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    clock.tick(FPS)
    display.update()
