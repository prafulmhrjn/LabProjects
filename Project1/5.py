'''5. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of
students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group
 has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of
  22 students. So, we need 32 desks in total.'''

class_a = int(input("Enter the number of students in class a:"))
class_b = int(input("Enter the number of students in class b:"))
class_c = int(input("Enter the number of students in class c:"))
desks_class_a = class_a//2
desks_class_b = class_b//2
desks_class_c = class_c//2
remaining_class_a = class_a%2
remaining_class_b = class_b%2
remaining_class_c = class_c%2
total_desks = desks_class_a + desks_class_b + desks_class_c + remaining_class_a + remaining_class_b + remaining_class_c
print(f"The total number of desks needed is {total_desks}")