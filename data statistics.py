#This program process a sequence of values input by user, and then
#outputs statistics pertaining to this input

valCount = 0             #number of values input by user
valSum = 0               #sum of input values
negatives = 0            #number of negative values
evens = 0                #number of even values
ynResponse = 'y'         #set to 'y' to allow first iteration of loop

while ynResponse == 'y' or ynResponse == 'Y':
    #obtain a value from the user
    value = float(input('Enter a value to be processed: '))

    #process the input value
    #first, add value to sum and increment value count
    valCount = valCount + 1
    valSum = valSum + value

    #next, determine if value is a new maximum or minimum value
    if valCount == 1:
        maxVal = value
        minVal = value
    else:
        if value < minVal:
            minVal = value
        else:
            if value > maxVal:
                maxVal = value

    #next, if value is negative, increment negative count
    if value < 0:
        negatives = negatives + 1

    #next, determine if value is an even integer number
    if value % 1 == 0:             #value is an integer
        if value % 2 == 0:         #value is even
            evens = evens + 1

    #determine if there is another value to be processed
    ynResponse = input('Do you have another value to be processed? (y/n): ')

#output requested statistics about input data
print('\nThe number of input values:', valCount)
print('The sum of the input values:', valSum)
print('The average of the input values entered:', (valSum / valCount))
print('The largest value entered:', maxVal)
print('The smallest value entered:' , minVal)
print('The number of negative values:', negatives)
print('The number of even numbers:', evens)
print('\nThank you for using this program\n')
