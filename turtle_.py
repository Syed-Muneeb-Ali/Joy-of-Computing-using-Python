import turtle
import random
turtle.bgcolor('black')

tur = turtle.Turtle()
tur.setpos(-250, 250)
dist = 25

tur.penup()
colors = ['white','red','yellow','green','blue','brown','violet','pink','orange','grey','cyan']
tur.color(random.choice(colors))

def spiral(n, m):
    startingRow = 0
    startingCol = 0
    endingRow = n
    endingCol = m
    
    while(startingRow < endingRow and startingCol < endingCol):
        for i in range(startingCol, endingCol):
            tur.dot()
            tur.forward(dist)
        startingRow+=1
        tur.right(90)
        tur.color(random.choice(colors))
        
        for i in range(startingRow, endingRow):
            tur.dot()
            tur.forward(dist)
        endingCol-=1
        tur.right(90)
        tur.color(random.choice(colors))
        
        for i in range(endingCol-1, startingCol-1, -1):
            tur.dot()
            tur.forward(dist)
        endingRow-=1
        tur.right(90)
        tur.color(random.choice(colors))
        
        for i in range(endingRow-1, startingRow-1, -1):
            tur.dot()
            tur.forward(dist)
        startingCol+=1
        tur.right(90)
        tur.color(random.choice(colors))
    
spiral(20, 20)
turtle.done()