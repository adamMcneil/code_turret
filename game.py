import pygame, sys, time, random

red = (255, 0, 0)        # red
green = (0, 255, 0)      # green
blue = (0, 0, 255)       # blue
yellow = (255, 255, 0)   # yellow
magenta = (255, 0, 255)  # magenta
cyan = (0, 255, 255)     # cyan
white = (255, 255, 255)  # white
black = (0, 0, 0)        # black

function_dict = {}
functions = []
wall_positions = []
w=1200
h=1200
num_of_square=5
player_x = 0
player_y = 0
player_facing = "up"
command_line = []
number_of_walls = 20

pygame.font.init()
font = pygame.font.SysFont("lato", 32)
text = font.render('', True, green)
textRect = text.get_rect()
textRect.center = (w//2, 25)



def read_walls_from_file():
   file = open("./levels/wall.lvl", "r")
   data = file.read()
   data_list = data.split("\n")
   global num_of_square
   num_of_square = int(data_list[0])
   for i in range(1, len(data_list)):
      new_position = data_list[i].split(" ")
      wall_positions.append((int(new_position[0]), int(new_position[1])))

read_walls_from_file()
length_of_square = w//num_of_square

DEFAULT_IMAGE_SIZE = (length_of_square, length_of_square)
arrow = pygame.image.load('./pictures/arrow.png')
cpu = pygame.image.load('./pictures/cpu.png')
virus = pygame.image.load('./pictures/virus.png')
start = pygame.image.load('./pictures/start.png')
wall = pygame.image.load('./pictures/wall.png')
arrow = pygame.transform.scale(arrow, DEFAULT_IMAGE_SIZE)
cpu = pygame.transform.scale(cpu, DEFAULT_IMAGE_SIZE)
virus = pygame.transform.scale(virus, DEFAULT_IMAGE_SIZE)
start = pygame.transform.scale(start, DEFAULT_IMAGE_SIZE)
wall = pygame.transform.scale(wall, DEFAULT_IMAGE_SIZE)

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

def draw_walls():
   for position in wall_positions:
      draw_on_grid(position[0], position[1], wall)

def make_walls():
   for i in range(number_of_walls):
      wall_positions.append((random.randint(0, num_of_square-1), random.randint(0, num_of_square-1)))

def move_player_forward():
   global player_x
   global player_y
   test_position = position_in_front_of_player()
   if not position_is_wall(test_position):
      player_x = test_position[0]
      player_y = test_position[1]

def check_position_x(new_x):
   global player_x
   if ((new_x, player_y) in wall_positions):
      return
   if new_x < 0 or new_x >= num_of_square:
      return
   player_x = new_x
   
def check_position_y(new_y):
   global player_y
   if ((player_x, new_y) in wall_positions):
      return
   if new_y < 0 or new_y >= num_of_square:
      return
   player_y = new_y

def position_in_front_of_player():
   if player_facing == "left":
      return (player_x-1, player_y)
   elif player_facing == "right":
      return (player_x+1, player_y)
   elif player_facing == "up":
      return (player_x, player_y-1)
   elif player_facing == "down":
      return (player_x, player_y+1)
   
def position_is_wall(position):
   return ((position[0], position[1]) in wall_positions) or position[0] < 0 or position[0] >= num_of_square or position[1] < 0 or position[1] >= num_of_square

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

def rotate_random():
   for i in range(random.randint(0,3)):
      rotate_player_right()

delay_sec = 0.1
def delay():
   time.sleep(delay_sec)

def update_screen():
   screen.fill(black)
   draw_player()
   draw_grid()
   draw_walls()
   screen.blit(text, textRect)
   pygame.display.update()

def execute_function(function_name):
   global text
   if function_name == "rotate":
      rotate_player_right()
      return
   if function_name == "forward":
      move_player_forward()
      return
   if function_name == "face_random":
      rotate_random()
      return
   
   for x in function_dict[function_name]:
      x = x.strip()
      text = font.render(x, True, green)
      if "jump if up" in x:
         if player_facing == "up":
            execute_function(x.split(" ")[3])
         else:
            execute_function(x.split(" ")[4])
      elif "jump if wall" in x:
         if position_is_wall(position_in_front_of_player()):
            execute_function(x.split(" ")[3])
         else:
            execute_function(x.split(" ")[4])
      else:
         execute_function(x)
         
      update_screen()
      delay()

def execute_main():
   execute_function("main")

def load_command_line():
   global command_line
   global functions
   global function_dict
   i = 0
   file = open(sys.argv[1], "r")
   data = file.read()
   data_list = data.split("\n")
   current_function_name = ""
   current_function_index = 0
   reading_function = False
   skip_one = False
   temp = []
   for x in data_list:
      if x == "end":
         reading_function = False
         function_dict[current_function_name] = temp
         temp = []
      elif "function" in x :
         current_function_name = x.split(" ")[1]
         reading_function = True
      elif reading_function:
         temp.append(x)
      
      i = i + 1
   print(function_dict)
   print(functions)

# make_walls()
update_screen()
load_command_line()
# execute_main()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_f:
            move_player_forward()
         if event.key == pygame.K_r:
            rotate_player_right()
         if event.key == pygame.K_e:
            execute_main()
         if event.key == pygame.K_w:
            execute_function("w")
         if event.key == pygame.K_a:
            execute_function("a")
         if event.key == pygame.K_s:
            execute_function("s")
         if event.key == pygame.K_d:
            execute_function("d")
         update_screen() 