import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, A, B, C, D in Query:
    ok = (A+B)*N >= C-D and (A-B)*N <= C+D
    print("Yes" if ok else "No")