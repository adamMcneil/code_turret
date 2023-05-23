import pygame, sys, time

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
player_facing = "up"
command_line = ["forward", "rotate", "forward","rotate", "forward","rotate", "forward", ]

DEFAULT_IMAGE_SIZE = (length_of_square, length_of_square)
arrow = pygame.image.load('arrow.png')
cpu = pygame.image.load('cpu.png')
virus = pygame.image.load('virus.png')
start = pygame.image.load('start.png')
arrow = pygame.transform.scale(arrow, DEFAULT_IMAGE_SIZE)
cpu = pygame.transform.scale(cpu, DEFAULT_IMAGE_SIZE)
virus = pygame.transform.scale(virus, DEFAULT_IMAGE_SIZE)
start = pygame.transform.scale(start, DEFAULT_IMAGE_SIZE)

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("HACK")

def draw_grid():
   for i in range(0, w, length_of_square):
      pygame.draw.line(screen, green, (i,0), (i,h), 2)
      pygame.draw.line(screen, green, (0,i), (w,i), 2)

def draw_on_grid(x, y, image):
   x = length_of_square * x
   y = length_of_square * y   
   screen.blit(image, (x,y))

def draw_player():
   draw_on_grid(player_x,player_y,arrow)

def move_player_forward():
   global player_x
   global player_y
   if player_facing == "left":
      player_x = player_x - 1
   if player_facing == "right":
      player_x = player_x + 1
   if player_facing == "up":
      player_y = player_y - 1
   if player_facing == "down":
      player_y = player_y + 1


def rotate_player_right():
   global player_facing
   global arrow
   if player_facing == "left":
      player_facing = "up"
   elif player_facing == "right":
      player_facing = "down"
   elif player_facing == "up":
      player_facing = "right"
   elif player_facing == "down":
      player_facing = "left"
   arrow = pygame.transform.rotate(arrow, -90)

delay_sec = 0.1
def delay():
   time.sleep(delay_sec)

def update_screen():
   screen.fill(black)
   draw_on_grid(3,3,start)
   draw_player()
   draw_grid()
   pygame.display.update()

def execute_command_line():
   for x in command_line:
      if x == "forward":
         move_player_forward()
      if x == "rotate":
         rotate_player_right()
      update_screen()
      delay()

   

update_screen()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_w:
            move_player_forward()
         if event.key == pygame.K_r:
            rotate_player_right()
         if event.key == pygame.K_e:
            execute_command_line()
         update_screen() 