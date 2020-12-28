import sys
input = sys.stdin.buffer.readline

N, M, T = map(int, input().rstrip().split())
AB = [list(map(int, input().rstrip().split())) for _ in range(M)]

def solve():
    t = N
    pre = 0
    for a, b in AB:
        t -= (a-pre)
        if t <= 0:
            return False
        t = min(t+(b-a), N)
        pre = b
    t -= (T-pre)
    if t <= 0:
        return False
    return True

print("Yes" if solve() else "No")