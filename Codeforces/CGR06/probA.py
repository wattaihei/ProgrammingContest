import sys
input = sys.stdin.readline

Q = int(input())
Query = [input().rstrip() for _ in range(Q)]

for S in Query:
    zeros = 0
    even = 0
    t = 0
    for s in S:
        n = int(s)
        if n%2 == 0:
            even += 1
        if n == 0:
            zeros += 1
        t += n
    if zeros > 0 and t%3 == 0 and even > 1:
        print("red")
    else:
        print("cyan")