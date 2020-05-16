import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = set()
for _ in range(K):
    D = int(input())
    A = list(map(int, input().split()))
    for a in A:
        S.add(a)

print(N-len(S))