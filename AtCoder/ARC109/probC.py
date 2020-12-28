import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
S = list(input().rstrip())

def winner(s1, s2):
    if s1 == s2:
        return s1
    if (s1, s2) in [("R", "P"), ("P", "S"), ("S", "R")]:
        return s2
    return s1

for _ in range(K):
    T = []
    for i in range(N):
        T.append(winner(S[(2*i)%N], S[(2*i+1)%N]))
    S = T

print(S[0])