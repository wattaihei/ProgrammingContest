N = int(input())

a = 0
n = 1
for n in range(1, N+1):
    a += n
    if a >= N:
        break
b = a - N
for i in range(1, n+1):
    if i != b:
        print(i)