def main():
    ynresponse='y'
    while ynresponse.lower()=='y':
        n=int(input("Which prime number you wish to find:"))

        def IsPrime(num):
            if num == 2 or num == 3:
                return True
            if num%2 == 0 or num<2:
                return False
            for x in range(3, int(num ** 0.5) + 1, 2):
                if num%x == 0:
                    return False
            return True

        def Prime(n):
            count=0
            match=0
            ynresponse = 'y'
            while ynresponse.lower() == 'y':
                if IsPrime(count) == True:
                    match+=1
                    if match == n:
                        return count
                        break
                    count += 1
                else:
                    match+=0
                    count+=1
        print (Prime(n))
        ynresponse = input('Would you like to enter another value?(y/n):')
        while ynresponse.lower() != 'y' and ynresponse.lower() != 'n':
            print('invalid input')
            ynresponse = input('Would you like to enter another value?(y/n):')
    print('Thank you for using this program!')


main()