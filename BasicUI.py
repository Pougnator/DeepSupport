#This file contains functions allowing user to interact with the model using keyboard
#It should only be used for testing purposes

def UserSelectIntent():
    choosenumber = input("Enter the number that correctly describes customers email: ")
    print("You have chosen number " + choosenumber)
    return choosenumber
if __name__ == '__main__':
    UserSelectIntent()