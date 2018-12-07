#This file contains functions allowing user to interact with the model using keyboard
#It should only be used for testing purposes

def UserSelectIntent():
    choosenumber = input("Enter the number that correctly describes customers email or enter -1 to add a new category: ")
    print("You have chosen number " + choosenumber)
    return choosenumber
if __name__ == '__main__':
    UserSelectIntent()