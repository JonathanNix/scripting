#import files
Items={'soap':1.30,'deoderant':2.30,'Razor':5.0,'toothbrush':1.50,'shaving cream':2.45,'advil':3.19}
Games=['Hi Lo']



def main():
    y=True
    print('*****Welcome to the Price is Right Mini-Game!*****')
    print()
    print('Below is a list of games to choose from. Once you decide what you would like to play, type in the name of that game below to play!')
    print()
    print('Enter "quit" to end game')
    print()
    for x in Games:
        print(x)
        print()
    while(True):
        ans=input('Choose game: ')
        if ans.lower().strip()=='hi lo':
            print()
            HiLo()
        elif ans=='2':
            main()
        elif ans=='3':
            main()
        elif ans=='4':
            main()
        elif ans=='quit':
            break
        else:
            print("That input is not valid. Please choose from the games above")


def HiLo():
    print('*****Hi Lo*****')
    print('Six grocery items are shown below. Choose the three most expensive items and win the bonus prize at the end!')
    print()
    for x in Items:
        print(x,end='     ')
    print('\n')
    top3original=sorted(Items, key=Items.get, reverse=True)[:3]
    top3=[]
    for x in top3original:
        top3.append(x.lower())
    print("Enter your choices for the 3 most expensive items")
    one=input('1: ')
    two=input('2: ')
    three=input('3: ')
    print()
    if one.lower().strip() in top3 and two.lower().strip() in top3 and three.lower().strip() in top3:
        return print('Congratulations!! You win the Bonus!\n')
    else:
        return print('Sorry that is incorrect :(\n')




main()
