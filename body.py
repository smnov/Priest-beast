import pygame, sys

pygame.init()
pygame.font.init() 
width, height = 924, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Priest Beast')
clock = pygame.time.Clock()

BG = pygame.transform.scale2x(pygame.image.load('background.png')).convert_alpha()
#Loop and exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Surface. (0, 0) - coordinates.
    screen.blit(BG,(0, 0))
    #Draw all our elements
    #Update everything
    pygame.display.update()
    clock.tick(60)