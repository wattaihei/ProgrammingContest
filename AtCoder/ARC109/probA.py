import sys
input = sys.stdin.buffer.readline

a, b, x, y = map(int, input().rstrip().split())
if a > b:
    ans = min((2*(a-b)-1)*x, (a-b-1)*y+x)
else:
    ans = min((2*(b-a)+1)*x, (b-a)*y+x)
print(ans)