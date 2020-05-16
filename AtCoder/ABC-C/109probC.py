from fractions import gcd

N, X = map(int, input().split()) # 横に2個
A = list(map(int, input().split()))
A.append(X)

A.sort()

D = [A[i+1]-A[i] for i in range(N)]

ans = D[0]
for d in D:
    ans = gcd(ans, d)

print(ans)