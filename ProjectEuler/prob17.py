N = 1000

NUM1 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
NUM10 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
NUM20 = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

A = [0]*(N+1)
for i in range(1, N+1):
    a, b = i//100, i%100
    c, d = b//10, b%10
    if c >= 2:
        A[i] += NUM20[c] + NUM1[d]
    elif c == 1:
        A[i] += NUM10[d]
    else:
        A[i] += NUM1[d]
    if a > 0:
        if a == 10:
            A[i] += 11
        elif b > 0:
            A[i] += NUM1[a] + 7 + 3
        else:
            A[i] += NUM1[a] + 7
print(sum(A))