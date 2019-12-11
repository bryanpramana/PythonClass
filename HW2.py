def main():
    number = float(input('Enter a value to be processed:'))
    count = 1
    sum = 0.0
    negativecount = 0
    evencount = 0
    smallest=number
    largest=number

    while True:
        loop = str(input('Do you have another value to be processed? (y/n):'))
        if loop.lower() =='y':
            count +=1
            sum += number
            if (number >= largest):
                largest = number
            else:
                if(number<=smallest):
                    smallest=number
            if (number < 0):
                negativecount +=1
            else:
                negativecount+=0
            if (number%2==0):
                evencount +=1
            else:
                evencount +=0
            number = float(input('Enter a value to be processed:'))
        else:
            sum += number
            if (number >= largest):
                largest = number
            else:
                if(number<=smallest):
                    smallest=number
            if (number < 0):
                negativecount += 1
            else:
                negativecount += 0
            if (number % 2 == 0):
                evencount += 1
            else:
                evencount += 0
            print('The number of input values:', count)
            print('The sum of the input values:', sum)
            print('The Average of the values entered:', sum/count)
            print('The largest value entered:',largest)
            print('The smallest value entered:', smallest)
            print('The number of negative values:', negativecount)
            print('The number of even values:', evencount)

            print('\nThank you for using this program')
            break

main()