import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    print("YES" if a%4 == 0 else "NO")