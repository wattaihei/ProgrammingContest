S = list(input())

A = []
c = 0
pre = '<'
for s in S:
    if pre == s:
        c += 1
    else:
        A.append(c)
        c = 1
    pre = s
A.append(c)

ans = 0
if A[0] != 0:
    l = len(A)
    for i in range(l):
        if i%2 == 0:
            if i != l-1:
                ans += max(A[i], A[i+1])
            else:
                ans += A[i]
    for a in A:
        ans += a*(a-1)//2
else:
    l = len(A)
    for i in range(l):
        if i % 2 == 0:
            if i != l-1:
                ans += max(A[i], A[i+1])
            else:
                ans += A[i]
    for a in A:
        ans += a*(a-1)//2
print(ans)