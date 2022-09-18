# My solutions to the Lessons on https://app.codility.com/programmers/lessons/1-iterations/
# Started saving my solutions late so I don't have the first few code

# Lesson 2, Exercise 2: OddOccurrencesInArray first solution (using list methods)
def solution(A):
    # write your code in Python 3.6
    for x in A:
        if A.count(x) % 2 == 1:
            return x

# time complexity of O(n^2), got a score of 66%, with a 100% correctness. the problem
# was the the time complexity. code is inefficient on larger arrays. so i came up with another solution

# Lesson 2, Exercise 2: OddOccurrencesInArray 2nd solution (using dictionaries) with a better time complexity
def solution(A):
    # write your code in Python 3.6
    B = {}
    for x in A:
        if x in B:
          B[x] += 1
        else:
            B[x] = 1

    for x in B:
        if B[x] % 2 == 1:
            return x  

# Lesson 3, Exercise 1: FrogJmp first solution
def solution(X, Y, D):
    # write your code in Python 3.6
    count = 0
    while X < Y:
        X += D
        count += 1
    return count

# Lesson 3, Exercise 1: FrogJmp second solution
import math
def solution(X, Y, D):
    # write your code in Python 3.6
    return math.ceil((Y-X)/D)

# Lesson 3, Exercise 2: PermMissingElem
def solution(A):
    # write your code in Python 3.6
    length = len(A)+2
    A.sort()
    B = list(range(1, length))
    for x in B:
        if x not in A:
            return x

# Lesson 3, Exercise 2: PermMissingElem second solution (using sets)
def solution(A):
    # write your code in Python 3.6
    length = len(A)+2
    A_set = set(A)
    for x in range(1, length):
        if x not in A_set:
            return x

# Lesson 3, Exercise 3: TapeEquilibrium 
def solution(A):
    # write your code in Python 3.6
    diff = []
    for index in range(1, len(A)):
        half_one = A[:index]
        half_two = A[index:]
        diff.append(abs(sum(half_one) - sum(half_two)))
    return min(diff)

# Lesson 3, Exercise 3: TapeEquilibrium second solution
def solution(A):
    # write your code in Python 3.6
    diff = []
    total = sum(A)
    splice = 0

    for x in range(len(A)-1):
        splice += A[x]
        diff.append(abs(total - (splice)* 2))
    return min(diff)

# Lesson 4, Exercise 1: FrogRiverOne


palindrome

find all palindrome substrings and store in a set

def palindrome(value):
    sIndex = 0
    endIndex = len(value) - 1
    
    while (sIndex < endIndex):
        if (value[sIndex] != value[endIndex]): 
            print(sIndex, endIndex)
            return False
        sIndex +=1
        endIndex -=1
    return True

print(palindrome("babab"))

# find the longest string in the set
a = {'e', 'oo', 'g', 'l', 'o'}
print(max(a))



# ROMAN NUMERALS
def roman(s):
    rDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s)):
        curr = rDict[s[i]]
        if i != len(s)-1 and rDict[s[i+1]] > curr:
            total -= curr
        else: total += curr

    return total

print(roman("III"))
print(roman("LVIII"))
print(roman("MCMXCIV"))




# Equilibrium Index

# This is a demo task.

# An array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e.
# A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
# Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.

# For example, consider the following array A consisting of N = 8 elements:

#   A[0] = -1
#   A[1] =  3
#   A[2] = -4
#   A[3] =  5
#   A[4] =  1
#   A[5] = -6
#   A[6] =  2
#   A[7] =  1
# P = 1 is an equilibrium index of this array, because:

# A[0] = −1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
# P = 3 is an equilibrium index of this array, because:

# A[0] + A[1] + A[2] = −2 = A[4] + A[5] + A[6] + A[7]
# P = 7 is also an equilibrium index, because:

# A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
# and there are no elements with indices greater than 7.

# P = 8 is not an equilibrium index, because it does not fulfill the condition 0 ≤ P < N.

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns any of its equilibrium indices. The function should return −1 if no equilibrium index exists.

# For example, given array A shown above, the function may return 1, 3 or 7, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

A = [-1, 3, -4, 5, 1, -6, 2, 1]

def solution(A):
    n = len(A)

    if (n == 0): return -1
    if (n == 1): return 0

    lower = 0
    higher = sum(A)

    for i in range(n):
        higher = higher - A[i]
        if higher == lower:
            return i
        lower = lower + A[i]

print(solution(A))

