from turtle import *


#we want to paint a house

speed(60)
#step 1: draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
color("yellow")
forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
color("blue")
goto(140,140)
pendown()
begin_fill
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
penup()
color("blue")
goto(60,140)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
exitonclick()