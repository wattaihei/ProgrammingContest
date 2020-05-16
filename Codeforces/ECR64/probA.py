N = int(input())
A = list(map(int, input().split()))

point = 0
for i in range(1, N):
    if A[i] == 1:
        if A[i-1] == 2:
            point += 3
        elif A[i-1] == 3:
            point += 4
    elif A[i] == 2:
        if A[i-1] == 1:
            if i == 1:
                point += 3
            elif A[i-2] == 3:
                point += 2
            else:
                point += 3
        elif A[i-1] == 3:
            point = -1
    else:
        if A[i-1] == 1:
            point += 4
        else:
            point = -1
            break
if point == -1:
    print('Infinite')
else:
    print('Finite')
    print(point)