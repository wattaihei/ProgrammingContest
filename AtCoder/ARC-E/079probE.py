import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
count = 0
B = [A[0]]
for i in range(N-1):
    a = A[i+1]+count
    C = []
    for b in B:
        x = (b-a)//(N+1)
        C.append(x)
    s = sum(C)
    count += s
    new_B = []
    for i, b in enumerate(B):
        new_B.append(b+s-(N+1)*C[i])
    new_B.append(a+s)
    B = new_B

delta = max(min(B) - N, 0)
count += delta*N
for i in range(N):
    B[i] -= delta

while max(B) > N-1:
    tmp = -1
    for i in range(N):
        if B[i] > tmp:
            tmp = B[i]
            ind = i
    for i in range(N):
        if i == ind:
            B[i] -= N
        else:
            B[i] += 1
    count += 1

print(count)
