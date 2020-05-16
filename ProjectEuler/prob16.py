A = [[0]*400 for _ in range(1001)]

A[0][0] = 1
for c in range(1000):
    for i in range(400):
        a = A[c][i]*2
        if a == 0: continue
        A[c+1][i] += a%10
        A[c+1][i+1] += a//10
print(sum(A[1000]))