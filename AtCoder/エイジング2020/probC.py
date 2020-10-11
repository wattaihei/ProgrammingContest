import sys
input = sys.stdin.readline

N = int(input())
ans = [0]*(N)

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            m = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if m <= N:
                ans[m-1] += 1

print(*ans, sep="\n")