import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().rstrip()

T = S[K-1:]
if (N-K+1)%2 == 0:
    T += S[:K-1]
else:
    T += S[:K-1][::-1]
print(T)