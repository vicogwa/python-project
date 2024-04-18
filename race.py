import turtle
import time
import random

WIDTH, HEIGHT = 500,300
COLORS= ['red', 'blue', 'black', 'pink', 'brown', 'cyan', 'orange', 'gold', 'indigo', 'gray']


def get_racers_number():
    racers = 0
    while True:
        racers = input("Enter the number of racers( 2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("input is not numeric... try again! ")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("number not in range 2-10. try again! ")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2-10:
                return colors[turtles.index(racer)]

            
def create_turtles(colors):
    turtles = []  
    spacingx = WIDTH// (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("circle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2)
        racer.pendown()
        turtles.append(racer)    
    return turtles    
            
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

racers = get_racers_number()
init_turtle()   

random.shuffle(COLORS)
colors = COLORS[: racers]

winner =race(colors)
print("the winner is the circle with color:", winner)
time.sleep(5)





