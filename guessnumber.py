from numbers import Number
import random 
import time 

num = random.randint(1,100)

def intro():
    name = input("Enter you name ")
    print(name , " we are going to play a game i am thinking of a number from 1 - 100 guess the number ")


    if num%2==0:
        print("the number is even ")
    else:
        print("the number is odd")
    print("guess a number")
def pick():
    guessTaken = 0 
    
    while guessTaken<6:
        enter = input("enter you guess: ")

        guess = int(enter)
        try :
            if guess<=100 and guess>=1:
                guessTaken = guessTaken+1 

                if guess>num:
                    print("The number you have guessed is too high ")

                if guess<num:
                    print("The number you have guessed is too low  ")

                if guess!=num:
                    print("Please try again!")

                if guess==num:
                    print("!!Congrats You Have Guessed The Correct Number!!")
                    break

            if guess>100 and guess<1:
                print("Please enter a number between 1 and 100")

        except:
            print("Enter a number , What you have entered is not a number ")
            

        
        





play = "yes"

while play == "yes":
    intro()
    pick()
    print("Would you like to play the guessing game again?")
    play = input("Enter yes or no")