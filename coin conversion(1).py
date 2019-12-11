#This program is used to convert a value specified in cents (0 - 99)
#to coins

#Begin by determining if there is a value to be converted
ynResponse = input('Do you have a value to convert to coins? ')

#Continue converting values each time user replies with "yes"
while ynResponse == 'yes':
    #obtain from user the value to be converted and make a copy
    coinValue = int(input('Enter coin amount: '))
    coinValueCopy = coinValue

    #convert input value to coins
    quarters = coinValue // 25
    coinValue = coinValue - (quarters * 25)

    dimes = coinValue // 10
    coinValue = coinValue - (dimes * 10)

    nickels = coinValue // 5

    pennies =  coinValue - (nickels * 5)

    #output the result in coins
    print(coinValueCopy, 'cents is equal to')
    print(quarters, 'quarters,')
    print(dimes, 'dimes,')
    print(nickels, 'nickels and')
    print(pennies, 'pennies')

    #ask the user if there is another amount to be converted
    ynResponse = input('\nDo you have another value to convert? ')
