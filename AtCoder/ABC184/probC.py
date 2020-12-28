import sys
input = sys.stdin.buffer.readline

r1, c1 = map(int, input().rstrip().split())
r2, c2 = map(int, input().rstrip().split())

def canreach(r, c):
    if r < 0: r = -r
    if c < 0: c = -c
    for (r3, c3) in [(1, 0), (0, 1), (1, 2), (2, 1), (3, 0), (0, 3)]:
        if r3-r == c3 - c:
            return True
    return False

ans = 0
if r1 == r2 and c1 == c2:
    ans = 0
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <= 3:
    ans = 1
elif (r1+c1)%2 == (r2+c2)%2 or canreach(r1-r2, c1-c2):
    ans = 2
else:
    ans = 3
print(ans)