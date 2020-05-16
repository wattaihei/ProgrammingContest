N, L = map(int, input().split())
A = list(map(int, input().split()))

s = 0
for i in range(N-1):
    if A[i] + A[i+1] > s:
        s = A[i] + A[i+1]
        ind = i

if s < L:
    print('Impossible')
else:
    print('Possible')
    for i in range(N-1):
        if i == ind:
            break
        print(i+1)
    for i in reversed(range(N-1)):
        if i == ind:
            break
        print(i+1)
    print(ind+1) 