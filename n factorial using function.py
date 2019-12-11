#Compute N! using function
def Factorial(nValue):
    nFactorial = 1

    for value in range(1, nValue +1):
        nFactorial *= value

    return nFactorial

#Obtain n value from user and compute and output n!
n = int(input('Enter value for n: '))
r = int(input('Enter value for r: '))

result = Factorial(n) // (Factorial(n - r) * Factorial(r))

print(n, '! / ((', n, '-', r, ')! ', r, '!) = ', result, sep='')
