"""--------------------------------------------------------------------------------------------------
                    Find US States Game
                    Student Name:   Vaishali Jorwekar
Problem Statement:  Find US states game using turtle graphics             
-------------------------------------------------------------------------------------------------"""
import turtle
from turtle import Screen,Turtle
import pandas as pd




###############################################################################
#   Function        :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Entry point
#   Author          :   Vaishali M Jorwekar
###############################################################################
def main():
    screen=Screen()
    screen.title("U.S.States Game")
    image="blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    correctState=0
    
    # Read States Name From CSV file
    stateFileData=pd.read_csv("50_states.csv")
    statesNameList=stateFileData["state"].to_list()
    guessedStateList=[]
    while len(guessedStateList) < 50:
        answerState = screen.textinput(title=f"{correctState}/50 correct",
                                       prompt="What's another state name ?")
        
        
        if answerState is None or answerState.title() == "Exit":
            missing_state_list=[state for state in statesNameList
                            if state not in guessedStateList]
            missingStatesData=pd.DataFrame(missing_state_list)
            missingStatesData.to_csv("state_to_learn.csv")
            break 
        if answerState.title() in statesNameList:
            correctState+=1   
            t=Turtle()
            t.hideturtle()
            t.penup()
            
            
            stateData=stateFileData[stateFileData.state==answerState]

            t.goto(stateData.x.item(),stateData.y.item())
            guessedStateList.append(answerState)
            t.write(stateData.state.item())
###############################################################################
#   Entry point of the program
###############################################################################
if __name__=="__main__":
    main()