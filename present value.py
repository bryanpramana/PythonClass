#Programming Assignment 1

#Obtain payment amount, term and interest rate data from user
paymentAmt = float(input('Please enter payment amount: '))
term = int(input('Enter term: '))
intRate = float(input('Enter interest rate: '))

#Compute present value
presentValue = paymentAmt * (1 - (1 + intRate) ** -term) / intRate

#Output result
print('\nGiven\nPayment Amount: $', format(paymentAmt, ',.2f'), sep='')
print('Interest Rate:', format(intRate, '.1%'))
print('Term:', term, 'years')
print('The present value is $', format(presentValue, ',.2f'), sep='')
