import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))

    F.sort(reverse=True)
    A.sort()
    l = -1
    r = 0
    for i in range(N):
        if A[i]*F[i] > r:
            r = A[i]*F[i]
    r += 1
    while r-l > 1:
        m = (r+l)//2
        q = []
        cost = 0
        for i in range(N):
            if F[i]*A[i] > m:
                cost += (F[i]*A[i]-m)//F[i]
                if (F[i]*A[i]-m)%F[i] != 0:
                    cost += 1
        if cost <= K:
            r = m
        else:
            l = m

    print(r)


if __name__ == "__main__":
    main()