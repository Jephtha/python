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
                  