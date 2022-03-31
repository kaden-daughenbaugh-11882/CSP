import turtle as trtl
import random as rand

#Maze Variables
angle = 90
number_walls = 25
wall_thickness = 3
path_width = 15
wall_length = path_width
colors = ['SkyBlue', 'LightCyan', 'PaleTurquoise', 'LightSeaGreen','Burlywood','MediumSlateBlue','MediumSlateBlue','DarkRed','DarkRed','BlueViolet']

#Drawing the Door Variable
def draw_door(pos):
  maze_writer.forward(pos)
  maze_writer.penup()
  maze_writer.forward(path_width*2)
  maze_writer.pendown()

#Draw the Barrier Variable
def draw_barrier(pos):
  maze_writer.forward(pos)
  maze_writer.left(angle)
  maze_writer.forward(path_width*2)
  maze_writer.backward(path_width*2)
  maze_writer.right(angle)


#initialize turtle
maze_writer = trtl.Turtle()
maze_writer.pensize(wall_thickness)
maze_writer.speed('fastest')

#draw a maze
for side in range(number_walls):
  wall_length += path_width
  maze_writer.color(rand.choice(colors))
  maze_writer.left(angle)

  if side > 4:

    #Locations for barriers and walls
    door = rand.randint(path_width*2, (wall_length - path_width*2))
    barrier = rand.randint(path_width*2, (wall_length - path_width*2))
    #If a new Door are rendered on Top of Each Other
    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2, (wall_length - path_width*2))

    if(door < barrier):
      draw_door(door)
      draw_barrier(barrier - door - path_width*2)
      #Draw the rest of the wall
      maze_writer.forward(wall_length - barrier)
    else:
      draw_barrier(barrier)
      draw_door(door - barrier)
      #Draw the rest of the wall
      maze_writer.forward(wall_length - door - path_width*2)

maze_writer.hideturtle()

#Creating the Screen and Background Events.
wn = trtl.Screen()
wn.bgcolor('white')
wn.mainloop()