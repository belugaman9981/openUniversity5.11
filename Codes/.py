import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
keep_running = True
pic = pygame.image.load("rain.jpg")

while keep_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_running = False

    screen.blit(pic, (0, 0))
    pygame.display.flip()
    
pygame.quit()