def HiLo(dict_main):
    print('*****Hi Lo*****')
    print('-'*30)
    print('Six grocery items are shown below. Choose the three most expensive items and win the bonus prize at the end!')
    print()

    dict_2={}
    for key in dict_main:
        if dict_main[key] < 15:
            dict_2[key]=dict_main[key]

    import random
    items = random.sample(dict_2.keys(),6)

    totaldictionary={}
    for x in items:
        totaldictionary[x]=dict_main[x]

    for x in range(len(items)):
        print(x+1,items[x])
    
    top3=sorted(totaldictionary, key=dict_main.get, reverse=True)[:3]

    print()
    print("Enter your choices for the 3 most expensive items")
    one=input('1: ')
    two=input('2: ')
    three=input('3: ')
    print()
    if one in top3 and two in top3 and three in top3:
        return print('Congratulations!! You win the Bonus!')
    else:
        return print('Sorry that is incorrect :(')


