#Compute N! using while loop

n = int(input("Enter value of n: "))

nCopy = n

nfactorial = 1
while n != 0:
    nfactorial *= n
    n -= 1

print(nCopy, '! = ', nfactorial, sep='')
