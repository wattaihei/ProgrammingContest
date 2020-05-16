import numpy as np

N, M, C = map(int, input().split()) # 横に2個
B = np.array(list(map(int, input().split()))) # 横に2個

c = 0
for i in range(N):
    Ai = np.array(list(map(int, input().split())))
    if Ai.dot(B) + C > 0:
        c += 1

print(c)
