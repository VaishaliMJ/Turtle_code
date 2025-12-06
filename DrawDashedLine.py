"""-----------------------------------------------------------------------------------------------------
                    Draw Dashed Line Turtle Module
                    (Student name - Vaishali Jorwekar)
                   
--------------------------------------------------------------------------------------------------------
Problem statement: Draw Dashed Line
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
#   Required Python Packages
#####################################################################################################
from turtle import Turtle,Screen
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
    for cnt in range(15):
        timmyTurtle.forward(10)
        timmyTurtle.penup()
        timmyTurtle.forward(10)
        timmyTurtle.pendown()
    screen=Screen()
    screen.exitonclick()
#####################################################################################################
#   Starter
#####################################################################################################
if __name__=="__main__":
    main()
