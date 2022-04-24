from pygame import *
font.init()

window = display.set_mode((700, 500))
display.set_caption('pong')

background = transform.scale(image.load("fon.png"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self)
        super().__init__ ()
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite('ball.png', 350, 250, 100, 80, 4)

finish = True          
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != False:
        window.blit(background, (0, 0))
        ball.reset()


    clock.tick(FPS)            
    display.update()