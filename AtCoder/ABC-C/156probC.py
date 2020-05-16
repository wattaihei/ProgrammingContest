import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 10**14
for t in range(101):
    s = 0
    for a in A:
        s += (a-t)**2
    ans = min(ans, s)
print(ans)