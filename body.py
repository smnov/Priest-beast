import pygame, sys

pygame.init()
pygame.font.init() 
width, height = 924, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Priest Beast')
clock = pygame.time.Clock()

BG = pygame.transform.scale2x(pygame.image.load('art/background.png')).convert_alpha()
Player_img1 = pygame.transform.scale2x(pygame.image.load('art/Player.png')).convert_alpha()
Player_rect = Player_img1.get_rect(center = (800, 300))
music = pygame.mixer.Sound('sound/music.mp3')



#Loop and exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    music.play()
    music.set_volume(0.1)
    # Player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        Player_rect.x += 4
    if keys[pygame.K_a]:
        Player_rect.x -= 4
    if Player_rect.x <= -30:
        Player_rect.x = -30
    if Player_rect.x >= 810:
        Player_rect.x = 810

    screen.blit(BG, (0, 0))
    screen.blit(Player_img1, Player_rect)

  

    #Update everything
    pygame.display.update()
    clock.tick(60)