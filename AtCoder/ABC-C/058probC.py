N = int(input())
Ss = [list(input()) for _ in range(N)]

A = Ss[0][:]
for S in Ss:
    B = []
    for s in S:
        if s in A:
            A.remove(s)
            B.append(s)
    A = B

A.sort()
print(''.join(A))