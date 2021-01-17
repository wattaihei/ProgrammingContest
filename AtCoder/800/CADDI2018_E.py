INF = 10**16

def make_dp(N, A):
    B = []
    C = [] # yoyuu
    for a0, a1 in zip(A, A[1:]):
        b = 0
        while a0 < a1:
            a0 *= 4
            b += 1
        c = 0
        while a0 >= a1*4:
            a1 *= 4
            c += 1
        B.append(b)
        C.append(c)

    stack1 = [(INF, 1)] # (前との余裕, 入ってる数)
    dp1 = [0]*N
    for i, (b, c) in enumerate(zip(B, C)):
        cnt = 0
        y = c
        dp1[i+1] += dp1[i]
        while stack1 and b > 0:
            d, j = stack1.pop()
            if b > d:
                cnt += j
                dp1[i+1] += d*cnt
                b -= d
            else:
                cnt += j
                dp1[i+1] += b*cnt
                y = d-b
                b = 0
        if b > 0:
            dp1[i+1] += b*cnt

        stack1.append((y, cnt+1))
    return dp1


def solve2(N, A):
    dp1 = make_dp(N, A)
    dp2 = make_dp(N, A[::-1])[::-1]

    ans = 10**18
    for i in range(N):
        ans = min(dp1[i]*2 + dp2[i]*2 + i, ans)

    return ans


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline

    N = int(input())
    A = list(map(int, input().rstrip().split()))

    print(solve2(N, A))