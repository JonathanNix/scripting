# The game begans by asking the user how many people are playing
# Next it asks the user to enter each player's name and puts it in a list
# The game gives out a random value for each user between 0 and 1000
# Each user has to guess the value
# If someone guesses the exact value, they win



# create a dictionary of objects with certain value
# randomly select from that dictionary an item
# user has to guess the value of that item
import time
import random
from random import randint
def wheelOfFortune(dic1):
    x = int(input("How many people are playing the game? "))
    list1 = []

    w = dic1.popitem()

    a1 = x
    while x > 0:
        y1 = input("What is the name of the player? ")
        list1.append(y1)
        x = x - 1





    a = ""

    if a1 == 1:
        try:
            y = w[1]
            print("It's time to pick the value of a/an ",w[0],".",sep="")
            print("You have 15 seconds to try and figure out what the value is.")
            print("The game will begin in 5 seconds.")
            time.sleep(5)
            print("Good luck!")
            a = 0
            l = 15
            now = time.time()
            future = now + l
            
            while time.time() < future:
                a = int(input("What is your guess? "))
                if a > y:
                    print("Your guess is to high!")
                elif a < y:
                    print("Your guess is to low!")
                else:
                    print("Thats right!")
                    a = y
                    break

                time.sleep(1)
                pass
            if a != y:
                print("The game is over. You ran out of time!")
            else:
                print("Good job, you won ",(y*2)," dollars, ",list1[0],"! The game is over.",sep="")

        except ValueError:
            print("The game is over.")


        

    elif a1 > 1:
        try:
            a2 = randint(1,a1)
            x = -1
            b = 0
            if a1 > 1:
                print("We need to decide who goes first.")
                print("The program has counted how many")
                print("players there are and selected a random number")
                print("between that amount of users and 1.")
                print("Whoever picks the number, goes first!")
                a3 = 0
                while x != a2:
                    print("Your turn ",list1[b],".",sep="")
                    x = int(input("Enter your number: "))

                    b = b + 1
                    if x != a2:
                        a3 = a3 + 1
                        pass
                    else:
                        break


            print(list1[a3],"has won and goes first.")
            print("The user/users after ",list1[a3]," will be randomly chosen by the computer.",sep="")
                    

            y = w[1]

            u = a3

            # Give user one shot and randomly select someone new after?
            
            print("It's time to pick the value of the object.")
            print("You have 25 seconds to try and figure out how much a/an ",w[0]," costs.",sep="")
            print("The game will begin in 5 seconds.")
            time.sleep(5)
            print("Good luck!")
         
            a = 0
            l = 1
            now = time.time()
            future = now + 25
            u = a3
            t = len(list1) - 1
            while time.time() < future:

                # while a != y:
                    print("It's your turn, ",list1[u],"!",sep="")
                    a = int(input("What is your guess? "))
                    if a > y:
                        print("That guess is to high!")
                    elif a < y:
                        print("That guess is to low!")
                    else:
                        print("That's right!")
                        break
                    time.sleep(1)
                    pass
                    u = randint(0,t)


            if a != y:
                print("No one guessed the price!")
            else:
                x = (y*2)
                print(list1[u]," got the price! They win ",x," dollars!",sep="")
                
        except ValueError:
            print("The game is over.")
    else:
        print("Find people!")

        
# dic1 = {"Xbox 360":150,"Xbox one":350,"Playstation 4":300,"Playstation 3":150,"Dark Souls 3 Collecters Edition":130,"NBA 2K17 Legendary Edition":80,"Uncharted 4":60,"Fallout 4":40}
# wheelOfFortune(dic1)
