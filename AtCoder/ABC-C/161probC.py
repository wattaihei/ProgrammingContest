import sys
input = sys.stdin.readline

N, K = map(int, input().split())

N %= K
print(min(N, K-N))