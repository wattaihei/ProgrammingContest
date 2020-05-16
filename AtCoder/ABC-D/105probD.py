from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

B = []
s = 0
for a in A:
    s = (s+a)%M
    B.append(s)

C = Counter(B)

ans = 0
for k, n in C.items():
    if k == 0:
        ans += (n+1)*n//2
    else:
        ans += (n-1)*n//2
print(ans)