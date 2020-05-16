import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

increase = [0 for _ in range(N)]

l = 0
r = 0
while l < N-1:
    if r < N-1:
        if A[r] <= A[r+1]:
            r += 1
        elif l == r:
            increase[l] = r
            r += 1
            l += 1
        else:
            increase[l] = r
            l += 1
    else:
        increase[l] = r
        l += 1

decrease = [0 for _ in range(N)]

l = 0
r = 0
while l < N-1:
    if r < N-1:
        if A[r] >= A[r+1]:
            r += 1
        elif l == r:
            decrease[l] = r
            r += 1
            l += 1
        else:
            decrease[l] = r
            l += 1
    else:
        decrease[l] = r
        l += 1

increase[N-1] = N-1
decrease[N-1] = N-1

for l, r in Query:
    if r <= increase[l]:
        a = 1
    else:
        a = 0
    if r <= decrease[l]:
        b = 1
    else:
        b = 0
    print(a, b)