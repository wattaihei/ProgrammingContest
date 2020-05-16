import collections 

N = int(input())
A = [int(input()) for _ in range(N)]

B = collections.Counter(A)

ans = 0
for k, v in B.items():
    ans += v%2

print(ans)