from Hangman import *
from QuizGame import *
from GuessingGame import *
from FootballSimulator import *


def OpenCentre():
    print("Welcome to the Entertainment Centre!!")
    UserInput = input("Choose an activity. Enter\n"
    "1 for Hangman \n2 for a Quiz\n3 for a Number Guessing Game\n4 for Football Simulator\n >> ")
    while UserInput not in ["1", "2", "3", "4"]:
        print("Please enter a valid option")
        UserInput = input("Choose an activity. Enter\n"
        "1 for Hangman \n2 for a Quiz\n3 for a Number Guessing Game\n4 for Football Simulator\n >> ")
            
    UserInput = int(UserInput)
    
    if UserInput == 1:
        PlayHangman()
    elif UserInput == 2:
        PlayQuiz()
    elif UserInput == 3:
        Guess()
    elif UserInput == 4:
        SimulateMatch()
    
    UserContinue = (input("\nEnter 'Yes' to play another game and 'No' to Exit >> ")).capitalize()
    while UserContinue not in ["Yes", "No"]:
        print("Please enter a valid option")
        UserContinue = (input("\nEnter 'Yes' to play another game and 'No' to Exit >> ")).capitalize()
    if UserContinue == "Yes":
        OpenCentre()
    elif UserContinue == "No":
        print("Thank you for using the Entertainment Centre. Have a great day!")


OpenCentre()
    
        
        
        
        
        