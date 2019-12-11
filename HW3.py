def main():
    ynresponse = 'y'
    while ynresponse.lower()=='y':
        while True:
            try:
                number = int(input('Enter a positive integer value:'))
                number = int(number)
                break
            except ValueError:
                print('Invalid input, please try again')
        while True:
            if(number<=0):
                number = int(input('Enter a positive integer value:'))
            else:
                break

        '''# This is the logic that i Use
        list = []
        for x in range(1,number):
            if(number%x==0):
                list.append(x)
            else:
                continue
        if(sum(list)==number):
            list.append(number)
            print(list)
        else:
            print('it is not a perfect number')
        '''
        listperfect=[]
        for x in range (1,number):
            list = []
            for y in range (1,x):
                if(x%y==0):
                    list.append(y)
                else:
                    continue
            if (sum(list) == x):
                listperfect.append(x)
            else:
                continue
        print('The list of all of the perfect numbers between 1 and the input value is ',listperfect)
        ynresponse = input('Would you like to enter another value?(y/n):')
        while ynresponse.lower() != 'y' and ynresponse.lower() != 'n':
            print('invalid input')
            ynresponse = input('Would you like to enter another value?(y/n):')
main()



