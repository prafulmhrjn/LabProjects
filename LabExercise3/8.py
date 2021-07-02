'''Q.No.8 Write a Python function that takes a number as a parameter and check the number
 is prime or not.'''

def prime_deter(i):
        if i==1:
            print('not a prime number')
        elif i==2:
            print('a prime number')
        elif i%2==0:
            print('not a prime number')
        else:
            print('a prime number')
i = int(input('Enter the number:'))
prime_deter(i)