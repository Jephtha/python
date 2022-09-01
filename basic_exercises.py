# Basic Python exercises from this website: https://pynative.com/python-basic-exercise-for-beginners/



# Exercise 3
# Write a program to accept a string from the user and display 
# characters that are present at an even index number.

# str = "pynative"

# for x in str:
#     if str.index(x) % 2 == 0:
#         print(x)



# Exercise 4
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# str = "pynative"

# def remove_chars(str, x):
#     print(str[x:]) 
# remove_chars(str, 2)



# Exercise 5
# Write a function to return True if the first and last number 
# of a given list is same. If numbers are different then return False.

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def first_last(a):
#     if a[0] == a[len(a)-1]:
#         print(True)
#     else:
#         print(False)

# first_last(numbers_x)
# first_last(numbers_y)



# Exercise 6
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# y = [10, 20, 33, 46, 55]

# for x in y:
#     if x % 5 == 0:
#         print(x)



# Exercise 7
# Write a program to find how many times substring x appears in the given string

# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma"))



# Exercise 8
# for x in range(5):
#     for y in range(x):
#         print(x, end="")
#     print("")


# Exercise 9
# Write a program to check if the given number is a palindrome number.

# x = 121
# y = 125

# def palindrome(a):
#     a = str(a)
#     b = a[::-1]
#     print("Yes") if a == b else print("No")

# palindrome(x)
# palindrome(y)



# Exercise 10
# Given a two list of numbers, write a program to create a new list such that the new list 
# should contain odd numbers from the first list and even numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# new_list = []

# for x in list1:
#     if x % 2 == 1: new_list.append(x)
# for x in list2:
#     if x % 2 == 0: new_list.append(x)

# print(new_list)



# Exercise 11
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# x = 7536
# x = str(x)
# print(" ".join(reversed(x)))


# Exercise 12
# x = 45000
# tax = 0
# if x <= 10000:
#     tax = x * 0
# elif x <= 20000:
#     tax = (x-10000) * 0.1 
# else: 
#     tax = (10000 * 0.1) + ((x-20000) * 0.2)
# print(tax)



# Exercise 13
# Print multiplication table form 1 to 10
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(x*y, end=" ")
#     print("")



# Exercise 14
# Print downward Half-Pyramid Pattern with Star (asterisk)
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print("")



# Exercise 15
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base, exp):
#     print(base ** exp)