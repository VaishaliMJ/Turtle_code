"""-----------------------------------------------------------------------------------------------------
                    Draw Shapes Using Turtle Module
                    (Student name - Vaishali Jorwekar)
                   
--------------------------------------------------------------------------------------------------------
Problem statement: Draw Shapes Using 
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
#   Required Python Packages
#####################################################################################################
import random
from turtle import Turtle,Screen
from random import randrange
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
    timmyTurtle.penup()
    timmyTurtle.setpos(-100,150)
    timmyTurtle.pendown()
    timmyTurtle.shape("turtle")
    timmyTurtle.color("blue")
    colors_shape=["dark violet","indian red","dark red","indigo","deep pink","dark green","blue"]
    screen=Screen()
    
    for shapeCnt in range(3,11):
        rand_color=random.choice(colors_shape)
        moveAngle=360/shapeCnt
        for sideCnt in range(shapeCnt):
            timmyTurtle.pencolor(rand_color)
            timmyTurtle.forward(80)
            timmyTurtle.right(moveAngle)
            timmyTurtle.forward(80)    
        
    
    screen.exitonclick()
#####################################################################################################
#   Starter
#####################################################################################################
if __name__=="__main__":
    main()
