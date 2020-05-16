N = int(input())
dic = {}
for _ in range(N):
    s = input()[0]
    if not s in dic.keys():
        dic[s] = 1
    else:
        dic[s] += 1

ans = 0
for v in dic.values():
    a1 = v//2
    a2 = v-a1
    ans += a1*(a1-1)//2 + a2*(a2-1)//2

print(ans)