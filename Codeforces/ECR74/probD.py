N = int(input())
S = list(input())

pre = S[0]
A = []
a = 0
for s in S:
    if s == pre:
        a += 1
    else:
        A.append(a)
        a = 1
    pre = s
A.append(a)

q = 0
for i in range(len(A)-1):
    q += A[i] + A[i+1] - 1

ans = N*(N-1)//2 - q
print(ans)