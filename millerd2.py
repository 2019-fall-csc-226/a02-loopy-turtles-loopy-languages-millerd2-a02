######################################################################
# Author: Dakota Miller
# Username: millerd2

# Assignment: A02: Exploring Turtles in Python
# Purpose: Draws a hexagon with a smile and eyes
######################################################################
import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
for i in range(8):
    bob.forward(100)
    bob.left(45)
jon = turtle.Turtle()
jon.penup() # moves the turtle up
jon.left(90) # rotates the turtle left
jon.forward(30) # moves the turtle on the screen
jon.right(90) # rotates turtle right
jon.pendown()
for j in range(10):
    jon.forward(10)
    jon.left(3)
alex = turtle.Turtle()
alex.penup()
alex.left(90)
alex.forward(180)
mike = turtle.Turtle()
mike.penup()
mike.left(90)
mike.forward(180)
mike.right(90)
mike.forward(100)
mike.left(90)
wn.exitonclick()