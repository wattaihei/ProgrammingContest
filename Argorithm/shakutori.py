N = int(input())
A = list(map(int, input().split()))

B = [0]
for a in A:
    B.append(B[-1]+a)

l = 0
r = 0
c = 0
while l < N+1 and r < N+1:
    if B[r] - B[l] == N:
        c += 1
        l += 1
    elif B[r] - B[l] > N:
        l += 1
    else:
        r += 1
print(c)