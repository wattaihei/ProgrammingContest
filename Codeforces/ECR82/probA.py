import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(input().rstrip()) for _ in range(Q)]

for S in Query:
    m = -1
    M = -1
    for i,s in enumerate(S):
        if s == "1":
            if m == -1:
                m = i
            M = i
    if m == -1:
        print(0)
    else:
        ans = 0
        for i in range(m, M):
            if S[i] == "0":
                ans += 1
        print(ans)