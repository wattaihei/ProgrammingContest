import sys
input = sys.stdin.buffer.readline

def main():
    A, B, C = map(int, input().rstrip().split())

    M = 101
    sdp = [[[0]*M for _ in range(M)] for _ in range(M)]

    sdp[A][B][C] = 1
    for a in range(A, M-1):
        for b in range(B, M-1):
            for c in range(C, M-1):
                s = a+b+c
                now = sdp[a][b][c]
                sdp[a+1][b][c] += a/s * (now)
                sdp[a][b+1][c] += b/s * (now)
                sdp[a][b][c+1] += c/s * (now)

    ans = 0
    for a in range(A, M):
        for b in range(B, M):
            for c in range(C, M):
                if (a == M-1 or b == M-1 or c == M-1):
                    ans += sdp[a][b][c] * (a+b+c - (A+B+C))

    print(ans)

if __name__ == "__main__":
    main()