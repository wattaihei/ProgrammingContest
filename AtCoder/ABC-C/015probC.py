N, K = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(N)]


def check(i, a):
    if i == N:
        if a == 0:
            return False
        else:
            return True
    F = True
    for t in Q[i]:
        Ans = check(i+1, a^t)
        F = F and Ans
    return F
ans = check(0, 0)
if ans:
    print('Nothing')
else:
    print('Found')