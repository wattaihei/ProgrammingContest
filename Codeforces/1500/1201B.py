N = int(input())
A = list(map(int, input().split()))

S = sum(A)
M = max(A)

if S%2 == 1 or M*2 > S:
    print('NO')
else:
    print('YES')