N, D = map(int, input().split()) # 横に2個
X = []
c = 0
for _ in range(N):
    Xi = list(map(int, input().split())) # １行に別れてるとき
    for x in X:
        dis = 0
        for i in range(D):
            dis += (x[i] - Xi[i])**2
        for k in range(200):
            if dis == k**2:
                c += 1
    X.append(Xi)

print(c)