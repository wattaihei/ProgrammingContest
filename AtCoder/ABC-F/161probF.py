import sys
input = sys.stdin.readline
import math

N = int(input())


def yaku(n):
    ret = []
    for num in range(1, int(math.sqrt(n)+3)):
        if n % num == 0:
            p = n//num
            if num < p:
                ret.append(num)
                ret.append(p)
            elif num == p:
                ret.append(p)
    return ret

ans = len(yaku(N-1))-1
for num in yaku(N):
    if num == 1: continue
    T = N
    while T%num == 0:
        T //= num
    if (T-1)%num == 0:
        ans += 1

print(ans) 