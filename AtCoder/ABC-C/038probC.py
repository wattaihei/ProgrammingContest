N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N-1):
    B.append(A[i+1]-A[i])

C = []
c = 0
for b in B:
    if b > 0:
        c += 1
        continue
    if c > 0:
        C.append(c)
        c = 0
if c > 0:
    C.append(c)

ans = N
for c in C:
    ans += c*(c+1)//2
print(ans)