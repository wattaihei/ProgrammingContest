from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

A.sort()
for i in reversed(range(N)):
    a = A[i]
    ia = bisect_left(A, a/2)
    a1, a2 = A[ia-1], A[ia]
    if a2 == a:
        b = a1
    elif min(a1, a-a1) > min(a2, a-a2):
        b = a1
    else:
        b = a2
    break
    
print(a, b)