from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

GCD1 = []
g = A[0]
for a in A:
    g = gcd(g, a)
    GCD1.append(g)

B = A[::-1]
g = B[0]
GCD2 = []
for b in B:
    g = gcd(g, b)
    GCD2.append(g)

ans = 1
for i in range(N):
    if i == 0:
        a = GCD2[N-2]
    elif i == N-1:
        a = GCD1[N-2]
    else:
        a = gcd(GCD1[i-1], GCD2[N-i-2])
    ans = max(ans, a)
print(ans)