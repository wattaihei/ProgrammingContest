import sys
input = sys.stdin.buffer.readline

N, K, mod = map(int, input().split())

def solve(n):
    dp = [[] for _ in range(N*K)]