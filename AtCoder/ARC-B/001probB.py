A, B = map(int, input().split())

ans = 40
for i in range(-4, 5):
    for j in range(-8, 9):
        m = A-B-(10*i + 5*j)
        ans = min(abs(i)+abs(j)+abs(m), ans)
print(ans)