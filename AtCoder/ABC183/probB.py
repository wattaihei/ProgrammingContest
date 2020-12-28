import sys
input = sys.stdin.buffer.readline

sx, sy, gx, gy = map(int, input().rstrip().split())

gy = -gy

print(-gy/(sy-gy)*(sx-gx) + gx)