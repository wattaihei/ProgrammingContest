import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
ans = (sum(A) - max(A) - min(A))/5
print(ans)