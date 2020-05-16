N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
R = [B[i]-A[i] for i in range(N)]

D = []
for i in range(N-1):
    D.append(A[i-1]+A[i+1])
D.append(A[N-2]+A[0])

for i, r in enumerate(R):
    