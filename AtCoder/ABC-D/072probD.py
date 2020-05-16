N = int(input())
A = list(map(int, input().split()))

c = 0
for i in range(N):
    if i+1 == A[i]:
        if i == N-1:
            c += 1
            break
        a, b = A[i], A[i+1]
        A[i] = b
        A[i+1] = a
        c += 1
        
print(c)