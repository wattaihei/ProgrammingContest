N = int(input())
A = list(map(int, input().split()))

up = True
down = True
Pass = False
c = 0
for i in range(N-1):
    if Pass:
        if i == N-2:
            c += 1
        Pass = False
        continue
    if up and A[i] > A[i+1]:
        c += 1
        if i == N-2:
            break
        if A[i+1] < A[i+2]:
            Pass = True
            up = True
            down = False
        else:
            up = False
            down = True
    elif down and A[i] < A[i+1]:
        c += 1
        if i == N-2:
            break
        if A[i+1] > A[i+2]:
            Pass = True
            up = False
            down = True
        else:
            up = True
            down = False
if up and down:
    c += 1
print(c)