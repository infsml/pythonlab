import pygame
import numpy as np
pygame.init()
white = (255, 255, 255)
X = 640
Y = 480
display_surface = pygame.display.set_mode((X, Y ))
a = np.arange(X)
b = np.arange(Y).reshape((Y,1))

Z = a+b<50
Z = Z.transpose()
Z = np.stack([Z]*3,axis=2)*255
surf = pygame.surfarray.make_surface(Z)

while True :
    display_surface.fill(white)
    display_surface.blit(surf, (0, 0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update()
