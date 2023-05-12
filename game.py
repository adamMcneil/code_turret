import pygame, sys

turret = pygame.image.load('turret.png')
DEFAULT_IMAGE_SIZE = (100, 100)
turret = pygame.transform.scale(turret, DEFAULT_IMAGE_SIZE)
turret = pygame.transform.rotate(turret, 90)
turret = pygame.transform.rotate(turret, 90)

w=600
h=600
x = w/2-turret.get_width()/2
y=h/2-turret.get_height()/2


pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("hello ben")

screen.blit(turret, (x,y))
pygame.display.update()


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()