def main():
    payment1=float(input('Please Enter the payment Amount: '))
    term=int(input('Please Enter the Term You Wish in Year: '))
    rate = float(input('Please Enter the Interest Rate: '))
    while True:
        if rate<0 or rate>1.0:
            rate = float(input('Please Enter the Interest Rate in the Range 0 to 1.0:'))
        else:
            Presentvalue=payment1*((1-(1+rate)**(-term))/rate)
            print('Given')
            print('Payment Amount:','${:,.2f}'.format(payment1))
            print('Interest Rate:', '{0:.1f}%'.format(rate * 100))
            print('Term:',term,'years')
            print('The present value is','${:,.2f}'.format(Presentvalue))
            break
main()
