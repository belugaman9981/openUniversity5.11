import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pic = pygame.image.load("rain.jpg")
i = True

while i:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = False
    screen.blit(pic, (0, 0))
    pygame.display.flip()
    
pygame.quit()