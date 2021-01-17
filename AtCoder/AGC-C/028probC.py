import sys
input = sys.stdin.buffer.readline


N = int(input())
A = []
for i in range(N):
    a, b = map(int, input().rstrip().split())
    A.append((a, i, 0))
    A.append((b, i, 1))

A.sort()

B1 = A[:N]
B2 = A[N:]

AB = [[-1, -1] for _ in range(N)]
s = 0
for b, i, t in B1:
    AB[i][t] = b
    s += b

for b, i, t in B2:
    AB[i][t] = -b

ok = False
left = []
right = []
for i, (a, b) in enumerate(AB):
    if (a < 0 and b < 0) or (a >= 0 and b >= 0):
        ok = True
        break
    if (a > 0):
        left.append(i)
    else:
        right.append(i)

if ok or (not left and right) or (left and not right):
    ans = s
else:
    ans = 10**18
    for b, i, t in B1:
        if B2[0][1] == i:
            score = s + B2[1][0] - b
        else:
            score = s + B2[0][0] - b
        ans = min(ans, score)

    if len(left) == 1:
        i = left[0]
        ans = min(ans, s - AB[i][1] - AB[i][0])
    if len(right) == 1:
        i = right[0]
        ans = min(ans, s - AB[i][1] - AB[i][0])

print(ans)