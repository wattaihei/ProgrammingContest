import sys
input = sys.stdin.buffer.readline

Q = int(input())
for _ in range(Q):
    a, b, c = map(int, input().split())
    ans = c + (c*b+c-1 +a-2)//(a-1)
    print(ans)