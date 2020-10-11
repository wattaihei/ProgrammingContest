import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = []
for i in range(N):
    inputstr = input().rstrip()
    if inputstr[0] == "b":
        x = int(inputstr.split()[1])
        S.append((x, i))
    else:
        x = 0
        ix = -1
        for y, j in S:
            if j + K < i and y > x:
                x = y
                ix = j
        S.remove((x, ix))
        S.append((x, i))
    print(x)