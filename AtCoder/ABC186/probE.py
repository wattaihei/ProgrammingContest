import sys
input = sys.stdin.buffer.readline


def solve(N, S, K):
    

Q = int(input())
for _ in range(Q):
    N, S, K = map(int, input().rstrip().split())
    print(solve(N, S, K))