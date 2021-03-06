import turtle
import sys
print("Let's play pool!")
wn=turtle.Screen()
wn.bgcolor("DarkSeaGreen4")
wn.title("Pool!")
start = 0
from tkinter import *  # Importing gui module
def button_function():  # The function that the button will run
	sys.exit()
def play():  # The function that the button will run
	start == 1
screen = Tk()  # Creating a screen
button_quit = Button(screen, text="Play", command=lambda:play)  # Creating a button
button_quit.pack()  # Putting the button on the screen
button2 = Button(screen, text="Quit", command=lambda:button_function())  # Creating another button
button2.pack()  # Putting that button on the screen
screen.mainloop  # Opening the screen
import pygame
from math import *
import random

pygame.init()
width = 660
height = 360
outerHeight = 400
margin = 30
display = pygame.display.set_mode((width, outerHeight))
pygame.display.set_caption("8 Ball Pool")
clock = pygame.time.Clock()

background = ("DarkSeaGreen1")

# Ball Class

stickColor = (249, 231, 159)

colors = ["yellow", "blue", "red", "purple", "orange", "green", "brown", "black", "yellow", "blue", "red", "purple", "orange", "green", "brown","CornflowerBlue"]

balls = []
noBalls = 15
radius = 10
friction = 0.1

# Ball Class
class Ball:
    def __init__(self, x, y, speed, color, angle, ballNum):
        self.x = x + radius
        self.y = y + radius
        self.color = color
        self.angle = angle
        self.speed = speed
        self.ballNum = ballNum
        self.font = pygame.font.SysFont("Agency FB", 10)

    # Draws Balls on Display Window
    def draw(self, x, y):
        pygame.draw.ellipse(display, self.color, (x - radius, y - radius, radius*2, radius*2))
        if self.color == "black" or self.ballNum == "cue":
            ballNo = self.font.render(str(self.ballNum), True, "CornflowerBlue")
            display.blit(ballNo, (x - 5, y - 5))
        else:
            ballNo = self.font.render(str(self.ballNum), True, "CornflowerBlue")
            if self.ballNum > 9:
                display.blit(ballNo, (x - 6, y - 5))
            else:
                display.blit(ballNo, (x - 5, y - 5))

    # Moves the Ball around the Screen
    def move(self):
        self.speed -= friction
        if self.speed <= 0:
            self.speed = 0
        self.x = self.x + self.speed*cos(radians(self.angle))
        self.y = self.y + self.speed*sin(radians(self.angle))

        if not (self.x < width - radius - margin):
            self.x = width - radius - margin
            self.angle = 180 - self.angle
        if not(radius + margin < self.x):
            self.x = radius + margin
            self.angle = 180 - self.angle
        if not (self.y < height - radius - margin):
            self.y = height - radius - margin
            self.angle = 360 - self.angle
        if not(radius + margin < self.y):
            self.y = radius + margin
            self.angle = 360 - self.angle

# Pocket Class
class Pockets:
    def __init__(self, x, y, color):
        self.r = margin/2
        self.x = x + self.r + 10
        self.y = y + self.r + 10
        self.color = color

    # Draws the Pockets on Pygame Window
    def draw(self):
        pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

    # Checks if ball has entered the Hole
    def checkPut(self):
        global balls
        ballsCopy = balls[:]
        for i in range(len(balls)):
            dist = ((self.x - balls[i].x)**2 + (self.y - balls[i].y)**2)**0.5
            if dist < self.r + radius:
                if balls[i] in ballsCopy:
                    if balls[i].ballNum == 8:
                        gameOver()
                    else:
                        ballsCopy.remove(balls[i])

        balls = ballsCopy[:]

#NEW CODE
def checkCueCollision(cueBall):
    for i in range(len(balls)):
        if collision(cueBall, balls[i]):
            if balls[i].x == cueBall.x:
                angleIncline = 2*90
            else:
                u1 = balls[i].speed
                u2 = cueBall.speed

                balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(cueBall.angle)))**2)**0.5
                cueBall.speed = ((u2*cos(radians(cueBall.angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                tangent = degrees((atan((balls[i].y - cueBall.y)/(balls[i].x - cueBall.x)))) + 90
                angle = tangent + 90

                balls[i].angle = (2*tangent - balls[i].angle)
                cueBall.angle = (2*tangent - cueBall.angle)

                balls[i].x += (balls[i].speed)*sin(radians(angle))
                balls[i].y -= (balls[i].speed)*cos(radians(angle))
                cueBall.x -= (cueBall.speed)*sin(radians(angle))
                cueBall.y += (cueBall.speed)*cos(radians(angle))




    # Applies force to Cue Ball
    def applyForce(self, cueBall, force):
        cueBall.angle = self.tangent
        cueBall.speed = force

    # Applies force to Cue Ball
    def applyForce(self, cueBall, force):
        cueBall.angle = self.tangent
        cueBall.speed = force

    # Draws Cue Stick on Pygame Window
    def draw(self, cuex, cuey):
        self.x, self.y = pygame.mouse.get_pos()
        self.tangent = (degrees(atan2((cuey - self.y), (cuex - self.x))))
        pygame.draw.line(display, "brown", (cuex + self.length*cos(radians(self.tangent)), cuey + self.length*sin(radians(self.tangent))), (cuex, cuey), 1)
        pygame.draw.line(display, self.color, (self.x, self.y), (cuex, cuey), 3)


# Checks Collision
def collision(ball1, ball2):
    dist = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dist <= radius*2:
        return True
    else:
        return False

# Checks if Cue Ball hits any Ball
def checkCueCollision(cueBall):
    for i in range(len(balls)):
        if collision(cueBall, balls[i]):
            if balls[i].x == cueBall.x:
                angleIncline = 2*90
            else:
                u1 = balls[i].speed
                u2 = cueBall.speed

                balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(cueBall.angle)))**2)**0.5
                cueBall.speed = ((u2*cos(radians(cueBall.angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                tangent = degrees((atan((balls[i].y - cueBall.y)/(balls[i].x - cueBall.x)))) + 90
                angle = tangent + 90

                balls[i].angle = (2*tangent - balls[i].angle)
                cueBall.angle = (2*tangent - cueBall.angle)

                balls[i].x += (balls[i].speed)*sin(radians(angle))
                balls[i].y -= (balls[i].speed)*cos(radians(angle))
                cueBall.x -= (cueBall.speed)*sin(radians(angle))
                cueBall.y += (cueBall.speed)*cos(radians(angle))


# Checks Collision Between Balls
def checkCollision():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            if collision(balls[i], balls[j]):
                if balls[i].x == balls[j].x:
                    angleIncline = 2*90
                else:
                    u1 = balls[i].speed
                    u2 = balls[j].speed

                    balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(balls[j].angle)))**2)**0.5
                    balls[j].speed = ((u2*cos(radians(balls[j].angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                    tangent = degrees((atan((balls[i].y - balls[j].y)/(balls[i].x - balls[j].x)))) + 90
                    angle = tangent + 90

                    balls[i].angle = (2*tangent - balls[i].angle)
                    balls[j].angle = (2*tangent - balls[j].angle)

                    balls[i].x += (balls[i].speed)*sin(radians(angle))
                    balls[i].y -= (balls[i].speed)*cos(radians(angle))
                    balls[j].x -= (balls[j].speed)*sin(radians(angle))
                    balls[j].y += (balls[j].speed)*cos(radians(angle))

def border():
    pygame.draw.rect(display, "brown", (0, 0, width, 30))
    pygame.draw.rect(display, "brown", (0, 0, 30, height))
    pygame.draw.rect(display, "brown", (width - 30, 0, width, height))
    pygame.draw.rect(display, "brown", (0, height - 30, width, height))

def score():
    font = pygame.font.SysFont("Agency FB", 30)

    pygame.draw.rect(display, (51, 51, 51), (0, height, width, outerHeight))
    for i in range(len(balls)):
        balls[i].draw((i + 1)*2*(radius + 1), height + radius + 10)

    text = font.render("Remaining Balls: " + str(len(balls)), True, stickColor)
    display.blit(text, (width/2 + 50, height + radius/2))


def reset():
    global balls, noBalls
    noBalls = 15
    balls = []

    s = 70

    b1 = Ball(s, height/2 - 4*radius, 0, colors[0], 0, 1)
    b2 = Ball(s + 2*radius, height/2 - 3*radius, 0, colors[1], 0, 2)
    b3 = Ball(s, height/2 - 2*radius, 0, colors[2], 0, 3)
    b4 = Ball(s + 4*radius, height/2 - 2*radius, 0, colors[3], 0, 4)
    b5 = Ball(s + 2*radius, height/2 - 1*radius, 0, colors[4], 0, 5)
    b6 = Ball(s, height/2, 0, colors[5], 0, 6)
    b7 = Ball(s + 6*radius, height/2 - 1*radius, 0, colors[6], 0, 7)
    b8 = Ball(s + 4*radius, height/2, 0, colors[7], 0, 8)
    b9 = Ball(s + 10*radius, height/2, 0, colors[8], 0, 9)
    b10 = Ball(s + 6*radius, height/2 + 1*radius, 0, colors[9], 0, 10)
    b11 = Ball(s + 2*radius, height/2 + 1*radius, 0, colors[10], 0, 11)
    b12 = Ball(s, height/2 + 2*radius, 0, colors[11], 0, 12)
    b13 = Ball(s + 4*radius, height/2 + 2*radius, 0, colors[12], 0, 13)
    b14 = Ball(s + 2*radius, height/2 + 3*radius, 0, colors[13], 0, 14)
    b15 = Ball(s, height/2 + 4*radius, 0, colors[14], 0, 15)

    balls.append(b1)
    balls.append(b2)
    balls.append(b3)
    balls.append(b4)
    balls.append(b5)
    balls.append(b6)
    balls.append(b7)
    balls.append(b8)
    balls.append(b9)
    balls.append(b10)
    balls.append(b11)
    balls.append(b12)
    balls.append(b13)
    balls.append(b14)
    balls.append(b15)



def gameOver():
    font = pygame.font.SysFont("Agency FB", 75)
    if len(balls) == 1:
        text = font.render("You Won!", True, (133, 193, 233))
    else:
        text = font.render("You Lost! Black in Hole!", True, (241, 148, 138))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_r:
                    poolTable()
        display.blit(text, (50, height/2))

        pygame.display.update()
        clock.tick()

def close():
    pygame.quit()
    sys.exit()

# Main Function

def poolTable():
    
    loop = True
    

    reset()

    noPockets = 6
    pockets = []

    p1 = Pockets(0, 0, "black")
    p2 = Pockets(width/2 - p1.r*2, 0, "black")
    p3 = Pockets(width - p1.r - margin - 4, 0, "black")
    p4 = Pockets(0, height - margin - 5 - p1.r, "black")
    p5 = Pockets(width/2 - p1.r*2, height - margin - 5 - p1.r, "black")
    p6 = Pockets(width - p1.r - margin - 5, height - margin - 5 - p1.r, "black")

    pockets.append(p1)
    pockets.append(p2)
    pockets.append(p3)
    pockets.append(p4)
    pockets.append(p5)
    pockets.append(p6)
      
poolTable()

wn.mainloop()