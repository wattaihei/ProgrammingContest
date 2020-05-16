N = int(input())
S = [int(input()) for _ in range(N)]

S.sort()
A = sum(S)
if A % 10 == 0:
    m = 0
    for s in S:
        if s % 10 != 0:
            m = s
            break
    A -= s
    if m == 0:
        A = 0
print(A)