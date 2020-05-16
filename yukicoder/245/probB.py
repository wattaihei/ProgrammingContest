import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]


for N, I, J in Query:
    k = min([I, J, N-1-I, N-1-J])
    a = 2*k*(2*N-2*k)
    I -= k; J -= k
    if I == 0:
        a += J
    elif J == N-1-2*k:
        a += J + I
    elif I == N-1-2*k:
        a += 2*(N-1-2*k) + (N-1-2*k-J)
    else:
        a += 3*(N-1-2*k) + (N-1-2*k-I)
    print(a)