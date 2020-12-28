
import sys
input = sys.stdin.readline

x, y, a, b = map(int, input().split())

ans = 0
while (a-1)*x < b and x*a < y:
    x *= a
    ans += 1

if x < y:
    ans += (y-1-x)//b
print(ans)