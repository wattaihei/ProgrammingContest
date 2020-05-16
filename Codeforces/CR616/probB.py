import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    left = -1
    right = -1
    for i, a in enumerate(A):
        if a >= i:
            left = i+1
        else:
            break
    for i, a in enumerate(A[::-1]):
        if a >= i:
            right = i+1
        else:
            break
    
    print("Yes" if left + right - 1 >= N else "No")