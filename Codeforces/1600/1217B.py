import sys
input = sys.stdin.readline

def main():
    Q = int(input())
    data = []
    for _ in range(Q):
        N, X = map(int, input().split())
        D = []
        A = []
        for _ in range(N):
            d, h = map(int, input().split())
            D.append(d-h)
            A.append(d)
        data.append((N, X, D, A))

    for N, X, D, A in data:
        d = max(D)
        b = max(A)
        score = X-b
        if score <= 0:
            print(1)
        elif d <= 0:
            print(-1)
        else:
            c = score//d + 1
            if score % d != 0:
                c += 1
            print(c)

if __name__ == "__main__":
    main()