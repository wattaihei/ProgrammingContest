from operator import itemgetter

N, M = map(int, input().split()) # 横に2個
City = [[i] + list(map(int, input().split())) for i in range(1, M+1)]


City = sorted(City, key=itemgetter(2))
City = sorted(City, key=itemgetter(1))

ans = []
pre = 1
seq = 0
for c in City:
    y = c[1]
    if y > pre:
        seq = 1
        pre = y
    else:
        seq += 1
    ans.append([c[0], y, seq])

ans.sort(key=itemgetter(0))
for a in ans:
    pre = str(a[1])
    seq = str(a[2])
    print('0'*(6-len(pre)) + pre + '0'*(6-len(seq)) + seq)