import sys
input = sys.stdin.buffer.readline




def make_inv(N, M, Field):
    inv = [[] for _ in range(M*N)]
    for n in range(N):
        for m in range(M):
            if Field[n][m] == ord("U"):
                inv[(n-1)*M+m].append(n*M+m)
            elif Field[n][m] == ord("D"):
                inv[(n+1)*M+m].append(n*M+m)
            elif Field[n][m] == ord("R"):
                inv[n*M+m+1].append(n*M+m)
            else:
                inv[n*M+m-1].append(n*M+m)
    return inv

def next(n, m, Field):
    s = Field[n][m]
    if s == ord("U"):
        return n-1, m
    if s == ord("D"):
        return n+1, m
    if s == ord("L"):
        return n, m-1
    elif s == ord("R"):
        return n, m+1
    return -1, -1

def Cycle(sn, sm, Field, N, M):
    D = [-1 for _ in range(M*N)]
    q = [(sn, sm)]
    D[sn*M+sm] = 0
    while q:
        qq = []
        for pn, pm in q:
            nn, nm = next(pn, pm, Field)
            if D[nn*M+nm] == -1:
                D[nn*M+nm] = D[pn*M+pm] + 1
                qq.append((nn, nm))
            else:
                return D[pn*M+pm] + 1 - D[nn*M+nm], nn, nm
        q = qq

def Coloring(sn, sm, cycle, invField, N, M, used, Color):
    Label = [0]*cycle
    q = [(sn, sm)]
    used[sn*M+sm] = True
    l = 0
    while q:
        qq = []
        for pn, pm in q:
            if Color[pn][pm] == ord("0"):
                Label[l%cycle] |= 1
            for mmm in invField[pn*M+pm]:
                nn, nm = mmm//M, mmm%M
                if not used[nn*M+nm]:
                    used[nn*M+nm] = True
                    qq.append((nn, nm))
        q = qq
        l += 1
    
    return sum(Label), used
    

def main():
    Q = int(input())
    ans = [None]*Q
    for ind in range(Q):
        N, M = map(int, input().split())
        Color = [list(input().rstrip()) for _ in range(N)]
        Field = [list(input().rstrip()) for _ in range(N)]

        invField = make_inv(N, M, Field)
        used = [False]*(M*N)
        a1 = 0
        a2 = 0
        for n in range(N):
            for m in range(M):
                if not used[n*M+m]:
                    cycle, sn, sm = Cycle(n, m, Field, N, M)
                    b, used = Coloring(sn, sm, cycle, invField, N, M, used, Color)
                    a1 += cycle
                    a2 += b
        ans[ind] = (str(a1) + " " +  str(a2))
    print("\n".join(ans))


if __name__ == "__main__":
    main()