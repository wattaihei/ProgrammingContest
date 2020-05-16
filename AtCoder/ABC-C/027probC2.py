N = int(input())

d = 0
c1, c2 = 1, 1
D = []
while c1 <= 2*N and c2 <= 2*N:
    if d%2 == 0:
        c1 = 2*c1
        c2 = 2*c2 + 1
        D.append(c1)
    else:
        c1 = 2*c1+1
        c2 = 2*c2
        D.append(c2)
    d += 1

for i, d in enumerate(D):
    if N < d:
        if i%2 == 0:
            ans = 'Aoki'
        else:
            ans = 'Takahashi'
        break
print(ans)