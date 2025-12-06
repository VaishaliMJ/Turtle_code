"""-----------------------------------------------------------------------------------------------------
                    Turtle Random walk And Color Turtle Module
                    (Student name - Vaishali Jorwekar)
                   
--------------------------------------------------------------------------------------------------------
Problem statement: Turtle Random walk and random color of Turtle Module
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
#   Required Python Packages
#####################################################################################################
import turtle as t
import random
turtle_directions=[0,90,180,270]
#####################################################################################################
#   Function Name    :  randomColor function 
#   Description      :  randomColor generator
#   Input Params     :  -   
#   Output Params    :  -
#   Author          :   Vaishali M Jorwekar
#   Date            :   6 Dec 2025
#####################################################################################################
def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
#####################################################################################################
#   Function Name    :  main function 
#   Description      :  main function
#   Input Params     :  -   
#   Output Params    :  -
#   Author          :   Vaishali M Jorwekar
#   Date            :   6 Dec 2025
#####################################################################################################
def main():
    timmyTurtle=t.Turtle()
    t.colormode(255) 
    timmyTurtle.shape("turtle")
    timmyTurtle.color(randomColor())
    timmyTurtle.pensize(10)
    timmyTurtle.speed("fastest")
    for i in range(150):
        timmyTurtle.forward(30)
        timmyTurtle.setheading(random.choice(turtle_directions))
        timmyTurtle.pencolor((randomColor())) 

    screen=t.Screen()
    screen.exitonclick()
#####################################################################################################
#   Starter
#####################################################################################################
if __name__=="__main__":
    main()
