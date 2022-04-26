import pygame, random, os

pygame.init()
pygame.font.init() 
width, height = 924, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Priest Beast')
clock = pygame.time.Clock()

BG = pygame.transform.scale2x(pygame.image.load('art/background.png')).convert_alpha()

music = pygame.mixer.Sound('sound/music.mp3')

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale2x(pygame.image.load('art/Player.png'))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 4
        if keys[pygame.K_a]:
            self.rect.x -= 4
        if player <= -30:
            self.rect.x = -30
        if player >= 810:
            self.rect.x = 810

class Enemy(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale2x(pygame.image.load('art/Enemy.png'))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def move(self):
        self.rect.x += 6
        if self.rect.x > 950:
            self.kill

#Loop and exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
   
    # Sounds
    music.play()
    music.set_volume(0.1)

    screen.blit(BG, (0, 0))

    player = Player(800, 220)
    player_list = pygame.sprite.Group()
    player_list.add(player)
    player_list.draw(screen)

    enemy = Enemy(100,200)    # spawn enemy
    enemy_list = pygame.sprite.Group()   # create enemy group
    enemy_list.add(enemy)  
    enemy_list.draw(screen) #refresh enemy

    #Update everything
    enemy_list.update()
    player_list.update()
    pygame.display.update()
    clock.tick(60)