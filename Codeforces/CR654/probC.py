import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

def solve(a, b, m, n):
    if a > b:
        d = a-b
        if m < d:
            a -= m
            m = 0
        elif m <= a+b:
            m -= d
            a -= d
        else:
            return False
    else:
        d = b-a
        if m < d:
            b -= m
            m = 0
        elif m <= a+b:
            m -= d
            b -= d
        else:
            return False
    
    if a != b:
        return min(a, b) >= n

    k = min(m, n)
    if a < k: return False

    a -= k
    b -= k
    m -= k
    n -= k

    if m > 0:
        return a+b >= m
    if n > 0:
        return min(a, b) >= n
    return True


for a, b, m, n in Query:
    print("Yes" if solve(a, b, m, n) else "No")