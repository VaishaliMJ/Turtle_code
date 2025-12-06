"""-----------------------------------------------------------------------------------------------------
                    Turtle Random walk Turtle Module
                    (Student name - Vaishali Jorwekar)
                   
--------------------------------------------------------------------------------------------------------
Problem statement: Turtle Random walk Turtle Module
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
#   Required Python Packages
#####################################################################################################
from turtle import Turtle,Screen
import random
pen_colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtle_directions=[0,90,180,270]
#####################################################################################################
#   Function Name    :  main function 
#   Description      :  main function
#   Input Params     :  -   
#   Output Params    :  -
#   Author          :   Vaishali M Jorwekar
#   Date            :   6 Dec 2025
#####################################################################################################
def main():
    timmyTurtle=Turtle()
    timmyTurtle.shape("turtle")
    timmyTurtle.color("blue")
    timmyTurtle.pensize(10)
    timmyTurtle.speed("fastest")
    for i in range(150):
        timmyTurtle.forward(30)
        timmyTurtle.setheading(random.choice(turtle_directions))
        timmyTurtle.pencolor(random.choice(pen_colours))
    screen=Screen()
    screen.exitonclick()
#####################################################################################################
#   Starter
#####################################################################################################
if __name__=="__main__":
    main()
