import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

for a in A:
    print("YES" if a//14 > 0 and 1 <= a%14 <= 6 else "NO")