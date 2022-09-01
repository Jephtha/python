# Python Input and Output Exercises from this website: https://pynative.com/python-functions-exercise-with-solutions/

# Exercise 1: Create a function in Python
# def func(name, age):
#     print(name, age)

# func("Jephthah", 21)

# Exercise 2: Create a function with variable length of arguments
# def func1(*var):
#     for i in var:
#         print(i)

# func1(20, 40, 60)

# Exercise 3: Return multiple values from a function
# def calculations(a, b):
#     return a+b, a-b

# x, y = calculations(40, 10)
# print(x, y)

# Exercise 4: Create a function with default argument
# def showEmployee(name, salary = 9000):
#     print(name, salary)

# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# Exercise 5: Create an inner function to calculate the addition in the following way
# def outer(a, b):
#     def inner(a, b):
#         return a+b
#     return 5 + inner(a, b)

# print(outer(5, 3))

# Exercise 6: Create a recursive function
# def recursive(n):
#     if n == 0:
#         return 0
#     else: 
#         return n + recursive(n-1)

# print(recursive(10))

# Exercise 7: Assign a different name to function and call it through the new name
# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)
# show_student = display_student
# show_student("Jephthah", 21)

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# print(list(range(4, 30, 2)))

# # Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))