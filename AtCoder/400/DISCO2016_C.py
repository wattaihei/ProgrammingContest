from fractions import gcd
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = {}
for a in A:
    k = gcd(a, K)
    if not k in B.keys():
        B[k] = 1
    else:
        B[k] += 1
#print(B)
ans = 0
for k1, c1 in B.items():
    for k2, c2 in B.items():
        if k1 < k2 and k1*k2 % K == 0:
            ans += c1*c2
        if k1 == k2 and k1*k2 % K == 0:
            ans += c1*(c1-1)//2
print(ans)