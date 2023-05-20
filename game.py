import pygame, sys

num_of_square=7
red = (255, 0, 0)        # red
green = (0, 255, 0)      # green
blue = (0, 0, 255)       # blue
yellow = (255, 255, 0)   # yellow
magenta = (255, 0, 255)  # magenta
cyan = (0, 255, 255)     # cyan
white = (255, 255, 255)  # white
black = (0, 0, 0)        # black

w=1200
h=1200
length_of_square = w//num_of_square

turret = pygame.image.load('turret.png')
fireball = pygame.image.load('fireball.png')
knight = pygame.image.load('knight.png')
DEFAULT_IMAGE_SIZE = (length_of_square, length_of_square)
turret = pygame.transform.scale(turret, DEFAULT_IMAGE_SIZE)
fireball = pygame.transform.scale(fireball, DEFAULT_IMAGE_SIZE)
knight = pygame.transform.scale(knight, DEFAULT_IMAGE_SIZE)

x = 3
y = 3

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("turret game")


screen.fill(white)


def draw_grid():
   for i in range(0, w, length_of_square):
      pygame.draw.line(screen, black, (i,0), (i,h))
      pygame.draw.line(screen, black, (0,i), (w,i))

def draw_on_grid(x, y, image):
   x = length_of_square * x
   y = length_of_square * y   
   screen.blit(image, (x,y))
   pygame.display.update()
   


for i in range(num_of_square):
   for j in range(num_of_square):
      draw_on_grid(i, j, knight)
draw_grid()
draw_on_grid(1, 2, fireball)
draw_on_grid(5, 5, turret)

pygame.display.update()


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      if event.type == pygame.KEYDOWN: 
         if event.key == pygame.K_a:
            turret = pygame.transform.rotate(turret, 90)
            screen.fill(white)
            screen.blit(turret, (x,y))
            draw_grid()
            pygame.display.update()
