import sys
input = sys.stdin.readline

def main():
    R, C, K = map(int, input().split())

    to_r = [[0 for _ in range(C)] for _ in range(R)]
    to_l = [[0 for _ in range(C)] for _ in range(R)]
    for j in range(R):
        A = list(input())
        w = 0
        for i, a in enumerate(A):
            if a == 'o':
                w += 1
                to_r[j][i] = w
            else:
                w = 0
        w = 0
        for i in range(C-1, -1, -1):
            b = A[i]
            if b == 'o':
                w += 1
                to_l[j][i] = w
            else:
                w = 0

    ans = 0
    for i in range(K-1, C-K+1):
        for j in range(K-1, R-K+1):
            a = min(to_r[j][i], to_l[j][i])
            if a <= K-1:
                continue
            ok = True
            for k in range(K):
                if min(to_r[j+k][i], to_l[j+k][i]) + k <= K-1 or min(to_r[j-k][i], to_l[j-k][i]) + k <= K-1:
                    ok = False
                    break
            if ok:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()