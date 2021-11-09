import pygame
pygame.init()
white = (255, 255, 255)
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Image')
image = pygame.image.load(r'google2.0.0.jpg')

colorama = {'[78, 129, 238, 255]':'blue','[255, 255, 255, 255]':'white'}

while True :
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            col = str(list(display_surface.get_at(pos)))
            if col in colorama:
                print(colorama[col])
            else:
                print('dunno')
        pygame.display.update()
