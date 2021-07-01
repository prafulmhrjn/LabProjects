''' 3. N students take K apples and distribute it among each other evenly. The remaining (the undivisible) part
 remains in the basket. How many apples will each student get? How many apples will remain in the basket?
 The program reads the number N and K. It should print two answers for the question above.'''


N = int(input("enter the number of students:"))
K = int(input("enter the number of apples:"))
each_student_get = K//N
rem = K%N
print(f"Each student gets {each_student_get} apples")
print(f"Remaining number of apples in the basket is {rem}")