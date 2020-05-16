import math

N, M = map(int, input().split())

MAX = M // N

def prime2(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor


def prob(i, s, ans):
    if i == len(A):
        if s <= MAX:
            ans = max(ans, s)
        return ans
    n, m = A[i]
    for j in range(m+1):
        ans = prob(i+1, s*n**j, ans)
    return ans

A = list(prime2(M).items())
ans = prob(0, 1, 1)
print(ans)