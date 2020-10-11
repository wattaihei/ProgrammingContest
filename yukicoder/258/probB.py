import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Sa = sum(A)
Sb = sum(B)

ans = -1
if N == 2:
    if Sa == Sb:
        ans = abs(A[0]-B[0])
elif Sa >= Sb and (Sa-Sb)%(N-2) == 0:
    ans = (Sa-Sb)//(N-2)
    for a, b in zip(A, B):
        if b < a - ans or (a - ans - b) % 2 != 0:
            ans = -1
            break

print(ans)