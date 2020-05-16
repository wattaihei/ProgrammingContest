N = int(input())
A = list(map(int, input().split()))

A.sort()
c = 0
for a in A:
    if a <= 0:
        c += 1

if c == N or c == N-1:
    ans = A[-1] - sum(A[:-1])
    print(ans)
    a, b = A[-1], A[0]
    for i in range(1, N):
        print(a, b)
        a, b = a-b, A[i]
elif c == 0 or c == 1:
    ans = sum(A[1:]) - A[0]
    print(ans)
    a, b = A[0], 0
    for i in range(1, N-1):
        a, b = a-b, A[i]
        print(a, b)
    a, b = A[-1], a-b
    print(a, b)
else:
    ans = sum(A[c:]) - sum(A[:c])
    print(ans)
    a, b = A[0], 0
    for i in range(N-c-1):
        a, b = a-b, A[c+i]
        print(a, b)
    a, b = A[-1], a-b
    print(a, b)
    for i in range(c-1):
        a, b = a-b, A[i+1]
        print(a, b)
    