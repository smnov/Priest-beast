import pygame, sys

pygame.init()
pygame.font.init() 
width, height = 924, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Priest Beast')
clock = pygame.time.Clock()

BG = pygame.transform.scale2x(pygame.image.load('art/background.png')).convert_alpha()
Player_img1 = pygame.transform.scale2x(pygame.image.load('art/Player.png')).convert_alpha()
Player_rect = Player_img1.get_rect(center = (400, 340))

class Player:
    def __init__(self):
        super().__init__()
        player_stand = Player_img1
        self.player_stand = player_stand
        self.rect = self.player_stand.get_rect(midbottom = (80,300))
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.gravity = -20

player = Player

#Loop and exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(BG,(0, 0))
    screen.blit(Player_img1, Player_rect)

    #Update everything
    pygame.display.update()
    clock.tick(60)