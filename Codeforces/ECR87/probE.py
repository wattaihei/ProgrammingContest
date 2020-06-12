import sys
input = sys.stdin.buffer.readline


N, M = map(int, input().split())
n1, n2, n3 = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def check():

    Color = [-1]*N
    P = []
    ok = True
    for n in range(N):
        if Color[n] != -1:
            continue
        q = [n]
        Color[n] = 0
        Cs = [[n], []]
        while q:
            qq = []
            for p in q:
                for np in graph[p]:
                    if Color[np] == -1:
                        qq.append(np)
                        Color[np] = Color[p]^1
                        Cs[Color[np]].append(np)
                    elif Color[np] != Color[p]^1:
                        ok = False
                        break
            q = qq
        P.append(Cs)
    return ok, P

def main():
    ok, P = check()
    dp = [[None]*(n2+1) for _ in range(len(P)+1)]
    dp[0][0] = 0
    for i in range(len(P)):
        a = len(P[i][0]); b = len(P[i][1])
        for n in range(n2+1):
            if not dp[i][n] is None:
                if n+a <= n2:
                    dp[i+1][n+a] = ~a
                if n+b <= n2:
                    dp[i+1][n+b] = b

    if not ok or dp[-1][n2] is None:
        print("NO")
    else:
        print("YES")
        tmp = n2
        Use2 = [-1]*N
        for i in reversed(range(len(P))):
            leng = dp[i+1][tmp]
            label = 1
            if leng < 0:
                label = 0
                leng = ~leng
            for n in P[i][label]:
                Use2[n] = 1
            for n in P[i][label^1]:
                Use2[n] = 0
            tmp -= leng
        ans = []
        num1 = 0
        for n, use2 in enumerate(Use2):
            if use2:
                ans.append("2")
            elif num1 < n1:
                num1 += 1
                ans.append("1")
            else:
                ans.append("3")
        print("".join(ans))

if __name__ == "__main__":
    main()