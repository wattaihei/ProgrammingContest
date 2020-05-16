M = int(input())
DC = [list(map(int, input().split())) for _ in range(M)]

ans = 0
p = 0
for d, c in DC:
    p += d*c
    ans += c

a = (p-1)%9+1
ans += (p-a)//9-1
print(ans)