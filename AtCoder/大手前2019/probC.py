from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = Counter(B)

checked = [0 for _ in range(100001)]
n = N+1
S = 0
for i, a in enumerate(A):
    c = C[a]
    if checked[a] != 0:
        c = max(0, c//(checked[a]+1))
    if c < n:
        lis = a
        n = c
    S += n
    checked[a] += 1
    print(n)