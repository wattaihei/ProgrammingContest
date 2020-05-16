N = int(input())
T, A = map(int, input().split()) # 横に2個
H = list(map(int, input().split()))

D = -1
for i, h in enumerate(H):
    tem = abs(T - h * 0.006 - A)

    if tem < D or i == 0:
        D = tem
        ans = i + 1
print(ans)
