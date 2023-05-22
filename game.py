import pygame, sys

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
num_of_square=7
length_of_square = w//num_of_square
player_x = 3
player_y = 3

DEFAULT_IMAGE_SIZE = (length_of_square, length_of_square)
arrow = pygame.image.load('arrow.png')
cpu = pygame.image.load('cpu.png')
virus = pygame.image.load('virus.png')
arrow = pygame.transform.scale(arrow, DEFAULT_IMAGE_SIZE)
cpu = pygame.transform.scale(cpu, DEFAULT_IMAGE_SIZE)
virus = pygame.transform.scale(virus, DEFAULT_IMAGE_SIZE)

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("HACK")

def draw_grid():
   for i in range(0, w, length_of_square):
      pygame.draw.line(screen, green, (i,0), (i,h))
      pygame.draw.line(screen, green, (0,i), (w,i))

def draw_on_grid(x, y, image):
   x = length_of_square * x
   y = length_of_square * y   
   screen.blit(image, (x,y))

def draw_player():
   draw_on_grid(player_x,player_y,arrow)

def update_screen():
   screen.fill(black)
   draw_player()
   draw_grid()
   pygame.display.update()

update_screen()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_a:
            player_x = player_x - 1
         if event.key == pygame.K_d:
            player_x = player_x + 1
         if event.key == pygame.K_w:
            player_y = player_y - 1
         if event.key == pygame.K_s:
            player_y = player_y + 1
         update_screen() 