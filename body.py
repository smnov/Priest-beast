import pygame, random

pygame.init()
pygame.font.init() 
width, height = 924, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Priest Beast')
clock = pygame.time.Clock()

BG = pygame.transform.scale2x(pygame.image.load('art/background.png')).convert_alpha()
music = pygame.mixer.Sound('sound/music.mp3')
bullet_list = []

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load('art/Player.png')).convert_alpha()
        self.x = x 
        self.y = y
        self.rect = self.image.get_rect(center = (800, 300))


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_d]:
            self.rect.x += 3
        if self.rect.x >= 810:
            self.rect.x = 810
        if self.rect.x <= -30:
            self.rect.x = -30
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        bullet_list.append(Bullet(self.x, self.y))

    def update(self):
        self.move()
        self.shoot()

class Enemy(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load('art/Enemy.png'))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def move(self):
        self.rect.x += 3
        if self.rect.x >= 900:
            self.kill()

    def update(self):
        self.move()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("art/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    
    def spawn(self):
        self.speed = -10
        self.x -= self.rect.x

    def update(self):
        if self.rect.x <= -100:
            self.kill()
        self.spawn()

        


player = pygame.sprite.GroupSingle(Player(800,200))

enemy_list = pygame.sprite.Group()  

obstacle_timer = pygame.USEREVENT + 1
timer = pygame.time.set_timer(obstacle_timer,4000)


hit = pygame.sprite.groupcollide(player, enemy_list, False, False)

#Loop and exit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == obstacle_timer:
            enemy_list.add(Enemy(random.randint(-1000, -30), 210))

		  
    # Sounds
    #music.play()
    #music.set_volume(0.1)

    screen.blit(BG, (0, 0))

    enemy_list.draw(screen) 
    enemy_list.update()


    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)