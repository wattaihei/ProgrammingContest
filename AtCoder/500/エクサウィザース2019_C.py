import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = input().rstrip()
TD = [list(map(str, input().split())) for _ in range(Q)]

l = 0
r = N
while r - l > 1:
    m = (l+r)//2
    right_over = False
    pl = m
    for t, d in TD:
        if S[pl] == t:
            if d == 'L':
                pl -= 1
                if pl == -1:
                    break
            else:
                pl += 1
                if pl == N:
                    right_over = True
                    break
    if right_over:
        r = m
    else:
        l = m

right = l

l = 0
r = N
while r - l > 1:
    m = (l+r)//2
    left_over = False
    pl = m
    for t, d in TD:
        if S[pl] == t:
            if d == 'L':
                pl -= 1
                if pl == -1:
                    left_over = True
                    break
            else:
                pl += 1
                if pl == N:
                    break
    if left_over:
        l = m
    else:
        r = m

left = l

print(right-left)