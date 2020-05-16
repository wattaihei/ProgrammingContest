N, K =  map(int, input().split())
A = list(map(int, input().split()))

p1 = A.index(1) + 1

l = (p1-1) // (K-1)
r = (N-p1) // (K-1)
amari = N - l*(K-1) - r*(K-1)

if N == K:
    ans = 1
elif N <= 2*K-1:
    ans = 2
elif amari == 1:
    ans = l + r
elif amari <= K:
    ans = l + r + 1
else:
    ans = l + r + 2
print(ans)