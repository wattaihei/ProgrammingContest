import sys
input = sys.stdin.buffer.readline

INF = 10**18

N = int(input())
A = list(map(int, input().rstrip().split()))


def solve(A, N):
    if max(A) <= 0:
        s = -INF
        for i, a in enumerate(A):
            if a > s:
                ind = i*2
                s = a
        ans = []
        for i in reversed(range(ind+1, N)):
            ans.append(i+1)
        for _ in range(ind):
            ans.append(1)
        return s, ans
    score0 = 0
    ans0 = []
    for a in A:
        if score0 == 0:
            if a <= 0:
                ans0.append(1)
                ans0.append(1)
            else:
                score0 += a
        else:
            if a > 0:
                ans0.append(2)
                score0 += a
            else:
                ans0.append(3)

    if N%2 == 0 or ans0[-1] == 3:
        ans0.append(2)
    return score0, ans0


A0 = A[::2]
A1 = A[1::2]

s0, ans0 = solve(A0, N)
s1, ans1 = solve(A1, N-1)
ans1 = [1] + ans1
if s0 > s1:
    print(s0)
    print(len(ans0))
    print(*ans0, sep="\n")
else:
    print(s1)
    print(len(ans1))
    print(*ans1, sep="\n")