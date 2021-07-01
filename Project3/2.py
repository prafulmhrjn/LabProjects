'''2. WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,
less than 40% –> fail'''


maths = float(input('Enter the marks of maths:'))
science = float(input('Enter the marks of science:'))
english = float(input('Enter the marks of english:'))
eph = float(input('Enter the marks of eph:'))
total_marks = maths+science+english+eph
print(f'The total marks is {total_marks}.')
percentage = (total_marks/400)*100
if percentage >70:
    print(f'distinction')
elif 60<percentage<70:
    print(f'first division')
elif 40<percentage<60:
    print(f'pass')
elif percentage<40:
    print(f'fail')