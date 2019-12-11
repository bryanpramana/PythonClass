#Compute N! using for loop

n = int(input("Enter value of n: "))

nfactorial = 1
for value in range(n):
    nfactorial *= (value + 1)

print(n, '! = ', nfactorial, sep='')
