N = int(input())
G = [int(input()) for _ in range(3)]

ans = 'NO'
qs = [N]
for _ in range(100):
    qqs = []
    for n in qs:
        for i in range(1, 4):
            m = n-i
            if (not m in qqs) and (not m in G):
                qqs.append(m)
            if m == 0:
                ans = 'YES'
                break
    if ans == 'YES':
        break
    qs = qqs
if N in G:
    ans = 'NO'
print(ans)