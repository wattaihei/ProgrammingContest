from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

AC = []
a = False
for i, s in enumerate(S):
    if s == 'A':
        a = True
        continue
    if a and s == 'C':
        AC.append(i-1)
    a = False

for l, r in LR:
    left = bisect_left(AC, l-1)
    right = bisect_right(AC, r-2)
    print(right-left)