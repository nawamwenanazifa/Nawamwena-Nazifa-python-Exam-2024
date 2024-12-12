#(i)
def circle_area(radius):
    pie = 3.14
    area = pie * (radius ** 2)
    return area

radius = 4
print(f"The area of the circle with radius {radius} is {circle_area(radius)}")


#(ii)
numbers = [4, 7, 2, 9, 12, 15]

sumOfNumbers = 0
for num in numbers:
    if num % 2 != 0:
        sumOfNumbers += num
print(f"The sum of odd numbers is: {sumOfNumbers}")



#(iii)
def calculate_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2

    if num2 != 0:
        quotient = num1 / num2
    else:
        quotient = "Undefined (division by zero)"

    print(f"\nResults:")
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")

calculate_operations()



#(v)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 26
student_info['city'] = 'Kampala'
print(student_info)


