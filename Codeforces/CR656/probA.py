import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    x, y, z = map(int, input().split())
    ans = []
    if (x == y) and x >= z:
        ans = [x, z, z]
    elif (y == z) and z >= x:
        ans = [x, x, y]
    elif (z == x) and x >= y:
        ans = [y, z, y]
    if not ans:
        print("NO")
    else:
        print("YES")
        print(*ans)