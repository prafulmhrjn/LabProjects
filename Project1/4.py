''' 4. Given the integer N - the number of minutes that is passed since midnight. How many hours and minutes are
 displaced on the 24 hr digital clock?
  The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes
   (between 0 and 59). For exampple if N = 150, the 150 minutes have passed since midnight- i.e. now is 2:30 am.
    So the
    program shgould print 2:30. '''

N = int(input("Enter the number of minutes passed since midnight:"))
hours = N//60
rem = N%60
print(f"{N} minutes have passed since midnight so the time displaced on the 24 hr digital clock is {hours}:{rem} ")