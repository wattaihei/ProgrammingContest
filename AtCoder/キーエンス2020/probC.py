N, K, S = map(int, input().split())

if S != 10**9:
    ans = [10**9]*(N-K) + [S]*K
else:
    ans = [1]*(N-K) + [S]*K

print(" ".join([str(a) for a in ans]))