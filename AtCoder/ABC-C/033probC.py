S = input()
N = len(S) // 2

A = []
k = 1
for i in range(N+1):
    if int(S[2*i]) == 0:
        k = 0
    if i == N:
        A.append(k)
        break
    if S[2*i+1] == '+':
        A.append(k)
        k = 1
print(sum(A))