Items={'soap':1.30,'deoderant':2.30,'razor':5.0,'toothbrush':1.50,'shaving cream':2.45,'advil':3.19}


def HiLo():
    print('*****Hi Lo*****')
    print('Six grocery items are shown below. Choose the three most expensive items and win the bonus prize at the end!')
    print()
    for x in Items:
        print(x,end='     ')
    print('\n')
    top3=sorted(Items, key=Items.get, reverse=True)[:3]
    #print(top3)
    print("Enter your choices for the 3 most expensive items")
    one=input('1: ')
    two=input('2: ')
    three=input('3: ')
    print()
    if one in top3 and two in top3 and three in top3:
        return print('Congratulations!! You win the Bonus!')
    else:
        return print('Sorry that is incorrect :(')


HiLo()
