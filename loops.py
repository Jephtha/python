# # Python Loops Exercises from this website: https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

# Exercise 1: Print First 10 natural numbers using while loop
# for i in range(1, 11):
#     print(i)
 
# Exercise 2: Print the following pattern
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# x = int(input("Enter a number: "))
# sum = 0
# for i in range(1, x+1):
#     sum += i
# print("sum: ", sum)

# Exercise 4: Write a program to print multiplication table of a given number
# num = 3
# for i in range(1, 11):
#     print(num * i)

# Exercise 5: Display numbers from a list using loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for x in numbers:
#     if x > 500:
#         break
#     elif x > 150:
#         continue
#     elif x % 5 == 0:
#         print(x)

# Exercise 6: Count the total number of digits in a number
# num = 75869
# count = 0
# for i in str(num):
#     count += 1
# print(count)

# Exercise 7: Print the following pattern
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()

# Exercise 8: Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# for i in range(len(list1)):
#     print(list1.pop())

# Exercise 9: Display numbers from -10 to -1 using for loop
# for i in range(-10, 0):
#     print(i)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done!")

# Exercise 11: Write a program to display all prime numbers within a range
# start = 25
# end = 50
# for i in range(start, end+1):
#     for j in range(2, i):
#         if (i % j) == 0:
#             break
#     else:
#         print(i)

# Exercise 12: Display Fibonacci series up to 10 terms
# fib = [0, 1]
# for i in range(1, 9):
#     fib.append(fib[i] + fib[i-1])
# print(fib)

# Exercise 13: Find the factorial of a given number
# factorial = 1
# for i in range(1, 6):
#     factorial *= i
# print(factorial)
                                                                                                                                                                           
# Exercise 14: Reverse a given integer number
# num = 76542
# print(''.join(list(reversed(str(num)))))

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list:
#     if my_list.index(i) % 2 != 0:
#         print(i)

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# for i in range(1, 7):
#     print(i*i*i)

# Exercise 17: Find the sum of the series upto n terms
# sum = 0
# for i in range(1, 6):
#     sum += int("2"*i)
# print(sum)

# # Exercise 18: Print the following pattern
# for i in range(1, 5):
#     print("*" * i)
#     if i == 4:
#         for j in range(5, 0, -1):
#             print("*"*j)