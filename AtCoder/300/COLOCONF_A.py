N = int(input())
S = list(input())

a = 0
A = []
for s in S:
    if s == 'A':
        a += 1
    else:
        if a > 0:
            A.append(a)
        a = 0

if a > 0:
    A.append(a)

if len(A) > 1:
    s = 0
    for i, a in enumerate(A):
        if i == 0 or i == len(A)-1:
            s += a*(a+1)//2
            continue
        s += N*a*(a+1)//2
    if S[0] == 'A' and S[-1] == 'A':
        d = A[0]+A[-1]
        s += (N-1)*d*(d+1)//2
    else:
        s += (N-1)*A[0]*(A[0]+1)//2
        s += (N-1)*A[-1]*(A[-1]+1)//2
elif len(A) == 1:
    if S[0] == 'A' and S[-1] == 'A':
        d = A[0]*N
        s = d*(d+1)//2
    else:
        s = N*A[0]*(A[0]+1)//2
else:
    s = 0

print(s)