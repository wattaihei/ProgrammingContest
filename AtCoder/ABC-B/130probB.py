N, X = map(int, input().split()) # 横に2個
L = list(map(int, input().split())) # １行に別れてるとき
L.append(0)

count = 0
D = 0
for i in range(N+1):
    if D <= X:
        count += 1
    D += L[i]


print(count)