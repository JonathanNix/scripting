


def HiLo(dict_main):
    dict_2={}
    
    for key in dict_main:
        if dict_main(key)<15:
            dict_2[key]=dict_main[key]
            
    print('*****Hi Lo*****')
    print('Six grocery items are shown below. Choose the three most expensive items and win the bonus prize at the end!')
    print()
    
    for x in dict_2:
        print(x,end='     ')
    print('\n')
    
    top3=sorted(dict_2, key=Items.get, reverse=True)[:3]
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



