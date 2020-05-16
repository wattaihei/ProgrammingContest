import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

checked = [False]*(10**5+1)

l = 0
r = 0
ans = 0
while r < N:
    if not checked[A[r]]:
        checked[A[r]] = True
        r += 1
    else:
        checked[A[l]] = False
        l += 1
    ans = max(ans, r-l)

print(ans)