"""-----------------------------------------------------------------------------------------------------
                        Draw a Spirograph 
                    (Student name - Vaishali Jorwekar)
                   
--------------------------------------------------------------------------------------------------------
Problem statement: Draw a Spirograph 
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
    timmyTurtle.speed("fastest")
    gapSize=5
    for cnt in range(int(360/gapSize)):
        timmyTurtle.color(randomColor())
        timmyTurtle.circle(100)
        timmyTurtle.setheading(timmyTurtle.heading()+10)

    screen=t.Screen()
    screen.exitonclick()
#####################################################################################################
#   Starter
#####################################################################################################
if __name__=="__main__":
    main()
