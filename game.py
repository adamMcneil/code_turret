import pygame, sys

red = (255, 0, 0)        # red
green = (0, 255, 0)      # green
blue = (0, 0, 255)       # blue
yellow = (255, 255, 0)   # yellow
magenta = (255, 0, 255)  # magenta
cyan = (0, 255, 255)     # cyan
white = (255, 255, 255)  # white
black = (0, 0, 0)        # black

turret = pygame.image.load('turret.png')
fireball = pygame.image.load('fireball.png')
DEFAULT_IMAGE_SIZE = (200, 200)
turret = pygame.transform.scale(turret, DEFAULT_IMAGE_SIZE)
fireball = pygame.transform.scale(fireball, DEFAULT_IMAGE_SIZE)
w=1200
h=1200
x = w/2-turret.get_width()/2
y=h/2-turret.get_height()/2


pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("hello ben")

color = (255, 255, 255)
screen.fill(color)

for i in range(0, w, 200):
   pygame.draw.line(screen, black, (i,0), (i,h))
   pygame.draw.line(screen, black, (0,i), (w,i))
   print (i)

screen.blit(turret, (x,y))
screen.blit(fireball, (x,y))
pygame.display.update()


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      if event.type == pygame.KEYDOWN: 
         if event.key == pygame.K_a:
            turret = pygame.transform.rotate(turret, 90)
            screen.fill(color)
            screen.blit(turret, (x,y))
            pygame.display.update()