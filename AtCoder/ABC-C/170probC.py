import sys
input = sys.stdin.readline

X, N = map(int, input().split())
A = list(map(int, input().split()))

B = set(A)
t = 10**15
ans = -1
for i in range(103):
    if not i in B and abs(i-X) < t:
        t = abs(i-X)
        ans = i

print(ans)