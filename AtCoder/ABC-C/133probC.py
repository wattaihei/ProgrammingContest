L, R = map(int, input().split()) # 横に2個

l = L // 2019
r = R // 2019
ll = L % 2019
rr = R % 2019

if l < r:
    ans = 0
else:
    ans = 2019
    for i in range(ll, rr+1):
        for j in range(i+1, rr+1):
            k = i * j % 2019
            ans = min(ans, k)

print(ans)