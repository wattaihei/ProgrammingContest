N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
for l in range(N):
    b = 0
    for r in range(l, N):
        b += A[r]
        B.append(b)
B.sort(reverse=True)
#print(B)

def trans2(n):
    A = bin(n)
    return str(A[2:])

C = []
maxl = 0
for i, b in enumerate(B):
    l = len(trans2(b))
    if i+1 <= K:
        maxl = l
    if i+1 > K and maxl != l:
        break
    C.append(trans2(b))
#print(C)
OK = [1 for _ in range(len(C))]

ans = 0
for l in range(maxl-1, -1, -1):
    update = []
    for i, c in enumerate(C):
        if c[-l-1] == '0' and OK[i] == 1:
            update.append(i)
            OK[i] = 0
    oks = sum(OK)
    if oks < K:
        for u in update:
            OK[u] = 1
    else:
        ans += 2**l
print(ans)
    