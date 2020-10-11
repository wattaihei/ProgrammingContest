import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

pre = 10**18
stock = 0
money = 1000
goup = False
for a in A:
    if a > pre:
        # buy in pre
        count = money//pre
        money -= count*pre
        stock += count
        goup = True
    else:
        if goup:
            money += stock*pre
            stock = 0
        goup = False
    pre = a

money += stock*A[-1]
print(money)