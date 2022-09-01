# Python Input and Output Exercises from this website: https://pynative.com/python-string-exercise/

# Exercise 1A: Create a string made of the first, middle and last character
# str1 = "James"
# print(str1[0] + str1[len(str1)//2] + str1[len(str1)-1])

# Exercise 1B: Create a string made of the middle three characters
# def split(str):
#     div = (len(str) - 3) // 2
#     print(str[div:div+3])

# split("JhonDipPeta")
# split("JaSonAy")

# Exercise 2: Append new string in the middle of a given string
# s1 = "Ault"
# s2 = "Kelly"
# mid = len(s1)//2
# print(s1[:mid] + s2 + s1[mid:])

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# s1 = "America"
# s2 = "Japan"

# mid1, mid2 = len(s1) // 2, len(s2) // 2
# print(s1[0] + s2[0] + s1[mid1] + s2[mid2] + s1[-1] + s2[-1])

# Exercise 4: Arrange string characters such that lowercase letters should come first
# str1 = "PyNaTive"
# temp = list(str1)
# for i in str1:
#     if i.isupper():
#         temp.pop(temp.index(i))
#         temp.append(i)
# print(''.join(temp))

# Exercise 5: Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"
# char, digit, symbol = 0, 0, 0
# for i in str1:
#     if i.isalpha():
#         char += 1
#     elif i.isnumeric():
#         digit += 1
#     elif i.isalnum() == False:
#         symbol += 1
# print(char, digit, symbol, sep = "\n")

# Exercise 6: Create a mixed String using the following rules
# s1 = "Abc"
# s2 = "Xyz"
# s3 = ''
# for i in range(len(s1)):
#     s3 += s1[i] + s2[-1-i]
# print(s3)

# Exercise 7: String characters balance Test
# def balance(s1, s2):
#     if s2.find(s1) == -1:
#         return False
#     else: return True
# print(balance("Ynf", "PYnative"))
# print(balance("Yn", "PYnative"))

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"
# print(str1.casefold().count("usa"))

# Exercise 9: Calculate the sum and average of the digits present in a string
# str1 = "PYnative29@#8496"
# sum, total = 0, 0
# for i in str1:
#     if i.isnumeric():
#         sum += int(i)
#         total += 1
# print(sum, sum/total)

# Exercise 10: Write a program to count occurrences of all characters within a string
# Exercise 11: Reverse a given string
# Exercise 12: Find the last position of a given substring
# Exercise 13: Split a string on hyphens
# Exercise 14: Remove empty strings from a list of strings
# Exercise 15: Remove special symbols / punctuation from a string
# Exercise 16: Removal all characters from a string except integers
# Exercise 17: Find words with both alphabets and numbers
# Exercise 18: Replace each special symbol with # in the following string


def gcd(a, b):
    for i in range(a, 2, -1):
        if (a % i == 0) & (b % i ==0):
            return i

print(gcd(24, 36))

def lcm(a, b):
    for x in range(1, 11):
        for y in range(1, 15):
            if b*x == a*y:
                return b*x

print(lcm(9, 12))
print(lcm(5, 15))
print(lcm(16, 24))
print(lcm(14, 22))

