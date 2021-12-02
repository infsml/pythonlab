import pygame
import numpy as np
pygame.init()
X,Y = 640,480
display = pygame.display.set_mode((X,Y))
x = np.arange(0,X)
y = np.arange(0,Y).reshape((Y,1))

#pts = [(50,50),(60,50),(60,60),(50,60)]
def makeR(r,x,y):
	w,h=25,50
	pos = np.array([320,240])
	pts = np.array([[-w,-h],[w,-h],[w,h],[-w,h]])
	r = r*np.pi/180
	rmatx = np.array([[np.cos(r),np.sin(r)],[-np.sin(r),np.cos(r)]])
	pts = (pts@rmatx)+pos
	(x1,y1),(x2,y2) = pts[-1],pts[0]
	Z = ((x-x1)*(y2-y1)<(y-y1)*(x2-x1))
	if len(pts)>2:
		for (x1,y1),(x2,y2) in zip(pts[:-1],pts[1:]):
			Z = Z * ((x-x1)*(y2-y1)<(y-y1)*(x2-x1))
	Z = 255*Z
	surf = pygame.surfarray.make_surface(Z.transpose())
	return surf
running = True
clk = pygame.time.Clock()

r=0
rv = 0.5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.blit(makeR(r,x,y), (0, 0))
    pygame.display.update()
    clk.tick(60)
    if r>180 or r<0:
    	rv = -rv
    r += rv
pygame.quit()