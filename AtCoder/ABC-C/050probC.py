from collections import Counter
N = int(input())
A = list(map(int, input().split()))
mod = int(1E9+7)

B = Counter(A)
c = (N+1)%2
#print(B, c)
ans = 1
for k, v in B.items():
    if k%2 != c or (k!=0 and v != 2):
        ans = 0
        break
    ans = ans * v % mod

print(ans)