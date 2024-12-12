#question3
#(i)
age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")
#(ii)
def grade_students(mark):
 mark = int(mark); 
if mark >= 90:
        return 'A'
elif mark >= 80:
        return 'B'
elif mark >= 70:
        return 'C'
elif mark >= 60:
        return 'D'
else:
        return 'F'
#(iii)
test_mark = 85
grade = grade_students(test_mark)
grade


#(iv)
valid_test_mark = 85
invalid_test_mark = 'Invalid Mark'

print(grade_students(valid_test_mark))  
print(grade_students(invalid_test_mark))

#(v)
def grade_students(scores):
    results = []
    for score in scores:
        if score >= 90:
            grade = 'A'
            message = 'Excellent'
        elif score >= 80:
            grade = 'B'
            message = 'Excellent'
        elif score >= 70:
            grade = 'C'
            message = 'Good'
        elif score >= 60:
            grade = 'D'
            message = 'Satisfactory'
        else:
            grade = 'F'
            message = 'Needs Improvement'
        results.append((grade, message))
    
    return results
scores = [95, 82, 74, 59, 88]
grades = grade_students(scores)
for grade, message in grades:
    print(f"Grade: {grade}, Message: {message}")
