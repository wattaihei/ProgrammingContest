import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

tmp = 0
zero = False
B = []
for a in A:
    if a < 0:
        tmp += 1
    elif a == 0:
        zero = True
    B.append(abs(a))

if tmp % 2 == 0 or zero:
    ans = sum(B)
else:
    ans = sum(B) - 2*min(B)

print(ans)