# Worksheet 1.2: Task 1 Solution

import sys

s_grade = input("Enter a grade from 1 - 100 : ")


if s_grade.isdecimal():
    
    grade = int(s_grade)

    if grade >= 0 and grade <= 100:
    
        if grade >= 70:
            result = "Distinction"

        elif grade <= 69 and grade >= 40:
            result = "Pass"

        else:
            result = "Fail"

    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")


print(f"{grade} is a {result}")