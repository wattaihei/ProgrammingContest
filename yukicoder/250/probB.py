import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

D = (a-c)**2 - 8*(b-d)
if D < 0:
    print("No")
elif D == 0:
    print("Yes")
else:
    print((a+c)/2, (b+d)/2)