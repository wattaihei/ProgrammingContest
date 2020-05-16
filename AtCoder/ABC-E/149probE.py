import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

Col = [0]*(3*10**5+1)
ind = 0
for i, a in enumerate(A):
    while ind <= a:
        Col[ind] = i
        ind += 1

while ind <= 3*10**5:
    Col[ind] = N
    ind += 1

l = 0
r = 2*10**5+1
while r-l > 1:
    m = (l+r)//2
    count = 0
    for i, a in enumerate(A):
        rem = m - a
        if rem < 0:
            count += N
        else:
            count += N - Col[rem]
    if count >= M:
        l = m
    else:
        r = m

b = 0
B = [0]
for a in A:
    b += a
    B.append(b)


# C以上になるのがMこある最小のC
C = l
ans = 0
Count = 0
for i, a in enumerate(A):
    rem = C-a
    if rem < 0:
        Count += N
        ans += B[N] + a*N
    else:
        c = Col[rem]
        pittari = Col[rem+1] - c
        Count += N-c
        ans += B[-1] - B[-(N-c)-1] + a*(N-c)

ans += (M-Count)*C
print(ans)