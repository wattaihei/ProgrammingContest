import sys
input = sys.stdin.readline

N, sx, sy = map(int, input().split())
A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]
for _ in range(N):
    x, y = map(int, input().split())
    if x == sx:
        if y > sy:
            B[0][0] += 1
        else:
            B[0][1] += 1
    elif y == sy:
        if x > sx:
            B[1][0] += 1
        else:
            B[1][1] += 1
    else:
        if x > sx and y > sy:
            A[0][0] += 1
        elif x > sx and y < sy:
            A[0][1] += 1
        elif x < sx and y > sy:
            A[1][0] +=1
        else:
            A[1][1] += 1

P = [
    (A[0][0]+A[0][1]+B[1][0], sx+1, sy),
    (A[0][0]+A[1][0]+B[0][0], sx, sy+1),
    (A[0][1]+A[1][1]+B[0][1], sx, sy-1),
    (A[1][0]+A[1][1]+B[1][0], sx-1, sy)
]

P.sort(reverse=True)
print(P[0][0])
print(P[0][1], P[0][2])