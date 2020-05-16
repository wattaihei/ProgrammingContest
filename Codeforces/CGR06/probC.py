import sys
input = sys.stdin.readline

R, C = map(int, input().split())
if R == 1 and C == 1:
    print(0)
elif R == 1:
    ans = list(range(2, C+2))
    print(*ans)
elif C == 1:
    ans = list(range(2, R+2))
    print(*ans, sep='\n')
else:
    for r in range(2, 2+R):
        print(r, end=" ")
        for c in range(2+R, 2+R+C-1):
            print(r*c, end=" ")
        print()