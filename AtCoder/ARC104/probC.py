import sys
input = sys.stdin.buffer.readline

INF = 10**18

N = int(input())
AB = [list(map(int, input().split())) for _ in range(B)]

def solve():
    left_singles = []
    right_singles = []
    twos = 0
    defined = [0]*(2*N+1)
    above = [-1 for _ in range(2*N+1)]
    for a, b in AB:
        if a != -1 and b != -1:
            defined[a] = b
            defined[b] = a
            for n in range(a, b+1):
                if above[n] != -1 and above[n] != b-a:
                    return False
                above[n] = b-a
        elif a != -1:
            left_singles.append(a)
            defined[a] = -1
        elif b != -1:
            right_singles.append(b)
            defined[b] = -1
        else:
            twos += 1
    left_singles.sort()
    right_singles.sort()
    updated = True
    while updated:
        updated = False
        new_left = []
        for n in left_singles:
            if above[n] != -1:
                updated = True
                m = n + above[n]
                if m > 2*N:
                    return False
                defined[n] = m
                defined[m] = n
                for b in range(n, m+1):
                    if above[b] != -1 and above[b] != above[n]:
                        return False
                    above[b] = above[n]
            else:
                new_left.append(n)
        new_right = []
        for n in right_singles:
            if above[n] != -1:
                updated = True
                m = n - above[n]
                if m < 1:
                    return False
                defined[n] = m
                defined[m] = n
                for b in range(m, n+1):
                    if above[b] != -1 and above[b] != above[n]:
                        return False
                    above[b] = above[n]
            else:
                new_right.append(n)
        left_singles = new_left
        right_singles = new_right
    