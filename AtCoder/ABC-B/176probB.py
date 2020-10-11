import sys
input = sys.stdin.readline

S = list(map(int, list(input().rstrip())))
print("Yes" if sum(S)%9 == 0 else "No")
