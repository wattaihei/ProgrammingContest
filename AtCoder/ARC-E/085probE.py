import sys
input = sys.stdin.buffer.readline

def solve1(N, A):
    A = [0] + A
    for i in reversed(range(1, N+1)):
        s = 0
        for j in range(i, N+1, i):
            s += A[j]
        if s < 0:
            for j in range(i, N+1, i):
                A[j] = 0
    
    return sum(A)

def solve2(N, A):
    ans = 0
    for bit in range(1<<N):
        s = 0
        nbit = 0
        for i in range(N):
            if (1<<i)&bit:
                for j in range(i, N, i+1):
                    nbit |= (1<<j)
        for i in range(N):
            if not (1<<i)&nbit:
                s += A[i]
        ans = max(s, ans)
    return ans

N = 10
A = [-8, -17, -7, -13, -13, 11, 10, 18, -20, 9]
solve1(N, A)

# import random
# while True:
#     N = 10
#     A = [random.randrange(-20, 20) for _ in range(N)]
#     ans1 = solve1(N, A)
#     ans2 = solve2(N, A)
#     if ans1 != ans2:
#         print(A)
#         print(ans1)
#         print(ans2)
#         break