'''Q.No.2 Write a function calledfizz_buzzthat takes a number.If the number is divisible by 3,
 it should return “Fizz”.If it is divisible by 5, it should return “Buzz”.If it is divisible by both 3 and 5,
  it should return “FizzBuzz”.Otherwise, it should return the same number.'''

def fizz_buzz():
    if x%3==0 and x%5==0:
        print('FizzBuzz')
    elif x%3==0:
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    else:
        print(f'{x}')
x = int(input('Enter the number:'))
fizz_buzz()