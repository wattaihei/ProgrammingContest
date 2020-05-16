from bisect import bisect_left

N, X = map(int, input().split())

L = [1]
P = [1]
l = 1
p = 1
for _ in range(N):
    l = 2*l+3
    p = 2*p+1
    L.append(l)
    P.append(p)
L.sort(reverse=True)
P.sort(reverse=True)
#print(L)
#print(P)
A = X
ans = 0
for n in range(0, N+1):
    if n == N:
        if A == 1:
            ans += 1
        break
    l0 = L[n]//2-1
    p0 = P[n]//2
    #print(A, l0, p0, ans)
    if A == 1:
        break
    elif  A == l0 + 2:
        ans += p0+1
        break
    elif A == 2*l0+3:
        ans += 2*p0+1
        break
    elif A < l0+2:
        A = A - 1
    elif A > l0+2:
        ans += p0+1
        A = A-l0-2
print(ans)
