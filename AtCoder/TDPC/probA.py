N = int(input())
P = list(map(int, input().split()))

max_a = 100*N
A = [False for _ in range(max_a+1)]
A[0] = True
for p in P:
    B = []
    for i in range(max_a+1):
        if i+p >= max_a:
            break
        if A[i]:
            B.append(i+p)
    for b in B:
        A[b] = True

print(sum(A))