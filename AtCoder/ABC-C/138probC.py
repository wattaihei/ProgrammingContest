N = int(input())
V = list(map(int, input().split()))
V.sort()

m = V[0]
for i in range(1, N):
    m = (V[i] + m)/2
print(m)