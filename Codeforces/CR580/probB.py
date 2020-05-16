import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
D = [0, 0, 0]
for a in A:
    if a < 0:
        ans += -1-a
        D[0] += 1
    elif a > 0:
        ans += a-1
        D[1] += 1
    else:
        D[2] += 1

if D[0] % 2 == 0:
    ans += D[2]
elif D[2] > 0:
    ans += D[2]
else:
    ans += 2

print(ans)