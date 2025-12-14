import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pic = pygame.image.load("Beluga_d.webp")
i = True

picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()

while i:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = False
            
    picx += 1
    picy += 1
    
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.flip()
    timer.tick(60)
    
pygame.quit()
