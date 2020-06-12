import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n,m,a,b in Query:
    if n%b == 0 and m%a == 0 and n//b == m//a:
        print("YES")
        cycle = n//b
        for c1 in range(cycle):
            for _ in range(b):
                S = ""
                for c2 in range(cycle):
                    if c1 == c2:
                        S += "1"*a
                    else:
                        S += "0"*a
                print(S)
    else:
        print("NO")