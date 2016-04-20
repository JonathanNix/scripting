dict_main={"apple":2,"chair":25,"soap":8,"comb":1.87,"milk":5,"coffe beans":10,"lotion":12}
import random

def check_out():
    print("Welcome! Let's play Check-Out!")
    print("-"*30)
    print()
    print("Here is how the game is played: The contestant bids on five items that are under $15 dollars each. If the total of the contestant’s bids is within $4.00 either way of the actual total of the items’ prices, then the contestant wins a brand new TELEVISION!!!")

    dict_2={}
    for key in dict_main:
        if dict_main[key] < 15:
            dict_2[key]=dict_main[key]

    
    items = random.sample(dict_2.keys(),5)
    
    dict_3={}
    print()
    print("-"*30)
    print("Here are the five items that you will bid on:")
    print()
    for x in items:
        print(x)
        dict_3[x]=dict_2[x]

    print()
    print("-"*30)
    
    sum_diff=0
    for item in dict_3:
        cont=True
        while cont:
            try:
                bid=float(input("What is your bid on the "+item+"? "))
            except ValueError:
                print("That is not a valid number. Please enter a number without dollar signs included.")
            else:
                print("The actual price is $",dict_3[item],sep='')
                diff=(float(dict_3[item])-bid)
                diff=float(format(diff,'0.2f'))
                print("You were $",diff," off from the actual price.",sep='')
                sum_diff+=diff
                cont=False

    print()
    print("-"*30)
    print()
    sum_diff=float(format(sum_diff,'0.2f'))
    if sum_diff>4 or sum_diff<-4:
        print("OH NO! Your bids were off a total of",sum_diff,"from the actual price total. You do not win the bonus prize.")
    else:
        print("CONGRATULATIONS!!! You were only",sum_diff,"off from the actual total. You have won a NEW TELEVISION!!!")
        
              

check_out()
