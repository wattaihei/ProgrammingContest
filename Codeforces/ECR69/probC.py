N, K = map(int, input().split())
A = list(map(int, input().split()))


if N == 1:
    print(0)
else:
    B = [A[i+1]-A[i] for i in range(N-1)]

    B.sort(reverse=True)
    print(sum(B[K-1:]))