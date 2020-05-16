N, D = map(int, input().split()) # 横に2個
A = 2*D+1
if N % A == 0:
    print(N//A)
else:
    print(N//A+1)