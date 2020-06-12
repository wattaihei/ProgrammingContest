import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

INF = 10**18

if 0 in A:
    ans = 0
else:
    ans = 1
    for a in A:
        ans *= a
        if ans > INF:
            ans = -1
            break
print(ans)