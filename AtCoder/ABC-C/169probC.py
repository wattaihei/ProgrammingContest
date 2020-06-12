import sys
input = sys.stdin.readline

AB = list(input().rstrip().split())
A = int(AB[0])
# print(AB)
B1, B0 = map(int, AB[1].split("."))
# B1 = int(B1s); B0 = int(B0s)
ans = A*B1 + A*B0//100
print(ans)