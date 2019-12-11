import string

Unacceptable = 0
Poor = 0
Weak = 0
Good = 0
Best = 0
ynresponse = input('Would you like to evaluate the quality of a password? (Y/N):')
while ynresponse.lower() != 'y' and ynresponse.lower() != 'n':
    print('invalid input')
    ynresponse = input('Would you like to evaluate the quality of a password? (Y/N):')

def PWRating(pw):
    number = 0
    char = 0
    for x in pw:
        char +=1
    if (char >= 8):
        number += 1
    for x in pw:
        if (x.islower()):
            number+=1
            break
    for x in pw:
        if (x.isupper()):
            number+=1
            break
    for x in pw:
        if (x.isnumeric()):
            number+=1
            break
    for x in pw:
        if x in string.punctuation:
            number+=1
            break
    return number

while ynresponse == 'y' or ynresponse == 'Y':
    password = input('Enter password:')
    if PWRating(password)==1:
        Unacceptable+=1
        print('Password:', password, ' Rating: Unacceptable(1)')
    if PWRating(password)==2:
        Poor+=1
        print('Password:', password, ' Rating: Poor(2)')
    if PWRating(password)==3:
        Weak+=1
        print('Password:', password, ' Rating: Weak(3)')
    if PWRating(password)==4:
        Good+=1
        print('Password:', password, ' Rating: Good(4)')
    if PWRating(password)==5:
        Best+=1
        print('Password:', password, ' Rating: Best(5)')

    ynresponse = input('Would you like to evaluate the quality of a password? (Y/N):')
    while ynresponse.lower() != 'y' and ynresponse.lower() != 'n':
        print('invalid input')
        ynresponse = input('Would you like to evaluate the quality of a password? (Y/N):')

print('Total number of passwords for each rating are:\n')
print('Best         : ', Best)
print('Good         : ', Good)
print('Weak         : ', Weak)
print('Poor         : ', Poor)
print('Unacceptable : ', Unacceptable)
print('Thank you for using this program')
