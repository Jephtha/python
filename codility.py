
def minpositive(a):
    A = set(a)
    ans = 1
    while ans in A:
       ans += 1
    return ans