import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
if K > N*(M-1)*2 + M*(N-1)*2:
    print("NO")
else:
    print("YES")
    ans = [(M-1, "R"), (M-1, "L")]
    for _ in range(N-1):
        ans.append((1, "D"))
        ans.append((M-1, "RUD"))
        ans.append((M-1, "L"))
    ans.append((N-1, "U"))

    num = 0
    P = []
    for n, S in ans:
        if n == 0: continue
        if num + n*len(S) <= K:
            P.append((n, S))
            num += n*len(S)
        else:
            rem = K - num
            p = rem//len(S)
            if p:
                P.append((p, S))
            ss = S[:rem%len(S)]
            if ss:
                P.append((1, ss))
            break
    print(len(P))
    for n, s in P:
        print(n, s)
