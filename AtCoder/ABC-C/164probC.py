import sys
input = sys.stdin.readline

N = int(input())
A = set()
for _ in range(N):
    S = input().rstrip()
    A.add(S)
print(len(A))