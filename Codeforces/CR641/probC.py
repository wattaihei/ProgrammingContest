
def main():
    import sys
    input = sys.stdin.buffer.readline

    N, M, Q = map(int, input().split())
    state = [list(input().rstrip()) for _ in range(N)]
    Query = [list(map(int, input().split())) for _ in range(Q)]


    Last = [[-1]*M for _ in range(N)]
    Need = [[-1]*M for _ in range(N)]
    q = []
    for n in range(N):
        for m in range(M):
            tmp = state[n][m]
            isStart = False
            if n != 0 and state[n-1][m] == tmp: isStart = True
            if n != N-1 and state[n+1][m] == tmp: isStart = True
            if m != 0 and state[n][m-1] == tmp: isStart = True
            if m != M-1 and state[n][m+1] == tmp: isStart = True
            if isStart:
                Need[n][m] = 0
                Last[n][m] = tmp-48
                q.append((n, m))

    if not q:
        for n,m,num in Query:
            print((state[n-1][m-1])%2)
    else:
        while q:
            qq = []
            for n, m in q:
                nexts = []
                if n != 0: nexts.append((n-1, m))
                if n != N-1: nexts.append((n+1, m))
                if m != 0: nexts.append((n, m-1))
                if m != M-1: nexts.append((n, m+1))
                for pn, pm in nexts:
                    if Last[pn][pm] == -1:
                        Last[pn][pm] = Last[n][m]
                        Need[pn][pm] = Need[n][m]+1
                        qq.append((pn, pm))
            q = qq
        
        for n, m, num in Query:
            n -= 1; m -= 1
            if num < Need[n][m]:
                print(state[n][m]%2)
            else:
                print((Last[n][m]+num)%2)
    
if __name__ == "__main__":
    main()