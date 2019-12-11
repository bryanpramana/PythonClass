# I am not quite sure with the assignment instruction,
# Whether students need to make a program that ask the user to input 3 data set at a time or one by one
# So I decided to make a program that ask and compute 3 data set a time
def main():

    #Asking the user to input 3 set of data's range

    print('Run 1:')
    num1 = int(input("Start Value 1 :"))
    num2 = int(input("End Value 1   :"))
    print('Run 2:')
    num3 = int(input("Start Value 2 :"))
    num4 = int(input("End Value 2   :"))
    print('Run 3:')
    num5 = int(input("Start Value 3 :"))
    num6 = int(input("End Value 3   :"))

    #Building the IsPrime Function to test whether a number prime or not

    def IsPrime(num):
        if num == 2 or num == 3:
            return True
        if num%2 == 0 or num<2:
            return False
        for x in range(3, int(num ** 0.5) + 1, 2):
            if num%x == 0:
                return False
        return True

    #Checking the first Data range set
    print('Run 1:\n')
    print("Enter a non-negative integer value:",num1)
    print('Enter a second non-negative integer value:',num2)
    print('The prime numbers between',num1,'and',num2,'are')
    if num1 != num2:
        count=0
        for y in range (num1,num2+1):
            if IsPrime(y) == True:
                print(y, end=' ')
                count += 1
                if (count % 5 == 0):
                    print('\n')
            else:
                continue
    else:
        if IsPrime(num1) == True:
            print(num1)
    print('\nThank you for using this program')

    #Checking the second Data range set
    print('Run 2:\n')
    print("Enter a non-negative integer value:",num3)
    print('Enter a second non-negative integer value:',num4)
    print('The prime numbers between',num3,'and',num4,'are')
    if num3 != num4:
        count=0
        for y in range (num3,num4+1):
            if IsPrime(y) == True:
                print(y, end=' ')
                count += 1
                if (count % 5 == 0):
                    print('\n')
            else:
                continue
    else:
        if IsPrime(num3) == True:
            print(num3)

    #Checking the third Data range set
    print('Run 1:\n')
    print("Enter a non-negative integer value:",num5)
    print('Enter a second non-negative integer value:',num6)
    print('The prime numbers between',num5,'and',num6,'are')
    if num5 != num6:
        count=0
        for y in range (num5,num6+1):
            if IsPrime(y) == True:
                print(y, end=' ')
                count += 1
                if (count % 5 == 0):
                    print('\n')
            else:
                continue
    else:
        if IsPrime(num5) == True:
            print(num5)
    print('\nThank you for using this program')

main()