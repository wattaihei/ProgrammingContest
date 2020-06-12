import sys
input = sys.stdin.readline

a ,b, c, d, e  = map(int, input().split())
ans = c*60+d - (a*60+b) - e
print(ans)