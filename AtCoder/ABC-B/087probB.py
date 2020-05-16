A = int(input())
B = int(input())
C = int(input())
X = int(input())

a = min(X//500, A)
b = min(X//100, B)
c = min(X//50, C)

ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500*i+100*j+50*k == X:
                ans += 1
print(ans)