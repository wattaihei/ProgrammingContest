N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0]
b = 0
for a in A:
    b += a
    B.append(b)

s = 0
for i in range(N-K+1):
    s += B[K+i] - B[i]
print(s)