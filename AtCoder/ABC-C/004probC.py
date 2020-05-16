N = int(input())

a = N // 5
b = N % 5

c = a % 6

A = [c+i if c+i <= 6 else c+i-6 for i in range(1,7)]

for i in range(b):
    a0 = A[i]
    a1 = A[i+1]
    A[i] = a1
    A[i+1] = a0

print(''.join([str(a) for a in A]))