'''10. Write a Python program to convert seconds to day, hour, minutes and seconds.'''

sec = int(input("Enter the number of seconds:"))
min = sec//60
rem_min = sec%60
hours = min//60
rem_hours = min%60
day = hours//24
rem_day = hours%24
print(f"The time is {day} days {rem_day} hours , {rem_hours} minutes and {rem_min} sec")