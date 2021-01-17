import sys
input = sys.stdin.readline

INF = 10**18

N = int(input())
A = list(map(int, input().rstrip().split()))

def once(A):
    m = -INF
    j = -1
    for i,a in enumerate(A):
        if a > m:
            m = a
            j = i
    if m <= N-1:
        return []
    for i in range(N):
        if i == j:
            A[i] -= N
        else:
            A[i] += 1
    return A


def solve1(A):
    ret = 0
    B = A[:]
    B.sort()
    C = [B.pop()]
    while B:
        b = B.pop()
        l = len(C)
        cmin = C[0]
        times = (cmin-b)//(N+1)
        delta = l*times
        D = []
        for c in C:
            D.append(c-times*(N-l+1))
        D.append(b+delta)
        while True:
            D.sort()
            if D[-1] - D[0] > N+1:
                delta += 1
                P = [D[-1]-N]
                for i in range(l):
                    P.append(D[i]+1)
                D = P
            else:
                break
        C = D
        B = list(map(lambda x: x+delta, B))
        ret += delta
    return ret, C


def solve(A):
    ans = 0
    # coll

    r, A = solve1(A)
    ans += r


    border = N
    m = min(A)
    d = max(m-border, 0)
    ans += d*N
    A = list(map(lambda x: x-d, A))
    while True:
        A = once(A)
        if not A:
            break
        ans += 1
    print(ans)


if __name__ == "__main__":
    solve(A)