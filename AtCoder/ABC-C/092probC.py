N = int(input())
A = list(map(int, input().split()))

B = [abs(A[i]) if i == 0 else abs(A[i]-A[i-1]) for i in range(N)]
B.append(abs(A[N-1]))

C = [abs(A[1]) if i == 0 else abs(A[i+1]-A[i-1]) for i in range(N-1)]
C.append(abs(A[-2]))

S = sum(B)

for i in range(N):
    print(S-B[i]-B[i+1]+C[i])