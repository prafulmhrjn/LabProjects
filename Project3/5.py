'''5. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print
 ‘zero’ if it is 0.'''

integer = int(input('Enter the integer:'))
if integer>0:
    print(f'True')
elif integer<0:
    print(f'False')
else:
    print(f'It is 0')