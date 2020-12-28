import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
A.sort()

ans = 0
s = 0
for i, a in enumerate(A):
    ans += a*i - s
    s += a
print(ans)