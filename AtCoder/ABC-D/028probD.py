N, K = map(int, input().split())
ans = (1 + 3*(N-1) + 6*(K-1)*(N-K)) / N**3
print(ans)