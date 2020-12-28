N, M = map(int, input().rstrip().split())

print((1900*M + 100*(N-M))*(2**M))