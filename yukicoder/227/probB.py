N = int(input())
A, B = 0, 0
AB = []
for _ in range(N-1):
    a, b = map(int, input().split())
    AB.append((a, b))
    A += a
    B += b

k1, k2 = 0, 0
count = [[0, 0] for _ in range(N-1)]
for j in range(N-1):
    a, b = AB[j]
    for i in range(N-1):
        if i == j:
            continue
        if count[i][0] + a <= AB[i][1]:
            count[i][0] += a
            a = 0
        elif count[i][0] <= AB[i][1]:
            a -= AB[i][1] - count[i][0]
            count[i][0] = AB[i][1]
    
        if count[i][1] + b <= AB[i][0]:
            count[i][1] += b
            b = 0
        elif count[i][1] <= AB[i][0]:
            b -= AB[i][0] - count[i][1]
            count[i][1] = AB[i][0]

    k1 += a
    k2 += b

ans = min(A-k1, B-k2) + 1
print(ans)