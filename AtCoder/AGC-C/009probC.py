import sys
input = sys.stdin.buffer.readline

def main():
    mod = 10**9+7
    INF = 2*10**18

    N, A, B = map(int, input().rstrip().split())
    X = [int(input()) for _ in range(N)]

    if A < B:
        A, B = B, A

    ok = True
    for x1, x2 in zip(X, X[2:]):
        if x2 - x1 < B:
            ok = False

    if not ok:
        print(0)
    else:
        # Aの最後がiである
        sdp = [0]*(N+1)
        sdp[0] = 1
        aind = 0
        zind = -1
        prex = -INF
        for i, x in enumerate(X):
            i += 1
            while aind+1 < i and x - X[aind] >= A:
                aind += 1

            if aind <= zind:
                sdp[aind] = 0
            
            sdp[i] = sdp[aind]

            if x - prex < B:
                zind = i-2
                sdp[i-1] = (sdp[i-1] - sdp[i-2]) % mod
                sdp[i-2] = 0
                
            sdp[i] = (sdp[i-1] + sdp[i]) % mod

            prex = x
        
        print(sdp[N])
    
if __name__ == "__main__":
    main()