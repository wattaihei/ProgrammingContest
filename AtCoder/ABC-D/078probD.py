import sys
input = sys.stdin.readline

def main():
    N, Z, W = map(int, input().split())
    A = list(map(int, input().split()))
    INF = 10**12

    ans = 0
    for i in range(N-1):
        s = INF
        for j in range(i+1, N):
            if j < N-1:
                s = min(s, abs(A[j]-A[N-1]))
            else:
                s = min(s, abs(A[j]-A[i]))
        ans = max(s, ans)

    ans = max(ans, abs(A[N-1]-W))

    print(ans)

if __name__ == "__main__":
    main()