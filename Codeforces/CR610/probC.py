import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, T, a, b  = map(int, input().split())
    Es = list(map(int, input().split()))
    Ts = list(map(int, input().split()))
    Query.append((N, T, a, b, Es, Ts))

for N, T, a, b, Es, Ts in Query:
    P = []
    remain_a = 0
    remain_b = 0
    for e, t in zip(Es, Ts):
        if e == 0:
            P.append((t, a))
            remain_a += 1
        else:
            P.append((t, b))
            remain_b += 1
    P.sort()
    t = 0
    ans = 0
    for i, (deadline, needtime) in enumerate(P):
        if t < deadline:
            remain_time = deadline - t - 1
            a_c = min(remain_time//a, remain_a)
            remain_time -= a_c*a
            b_c = min(remain_time//b, remain_b)
            ans = max(ans, i+a_c+b_c)
        t += needtime
        if needtime == a:
            remain_a -= 1
        else:
            remain_b -= 1

    if t <= T:
        ans = N
    print(ans)
