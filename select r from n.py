#Compute result of selecting r things from n

#Obtain n value from user and compute and output n!
n = int(input('Enter value for n: '))
r = int(input('Enter value for r: '))

nFactorial = 1
for value in range(1, n+1):
    nFactorial *= value

nrFactorial = 1
for value in range(1, (n - r + 1)):
    nrFactorial *= value

rFactorial = 1
for value in range(1, r + 1):
    rFactorial *= value

result = nFactorial // (nrFactorial * rFactorial)

print(n, '! / ((', n, '-', r, ')! ', r, '!) = ', result, sep='')

