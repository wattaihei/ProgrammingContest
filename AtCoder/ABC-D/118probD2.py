from operator import itemgetter

N, M = map(int, input().split())
A = list(map(int, input().split()))

COUNT = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

A.sort()

min_N = 100 # 一番使うのが少ない本数
dic = {} # 本数から数字
for a in A:
    min_N = min(min_N, COUNT[a])
    dic[COUNT[a]] = a

d = N//min_N
r = N%min_N
ans = {dic[min_N]: d}

B = sorted(list(dic.items()), key=itemgetter(1), reverse=True) # 数字の大きい方から
changed = 0
for c, num in B:
    if c == min_N:
        continue
    delta = c-min_N
    rep = r // delta
    if rep == 0:
        continue
    elif rep + changed > d:
        ans[num] = d - changed
        ans[dic[min_N]] -= d - changed
        break
    else:
        ans[num] = rep
        ans[dic[min_N]] -= rep
        changed += rep
        r -= delta*rep

C = sorted(list(ans.items()), key=itemgetter(0), reverse=True)
for num, c in C:
    print(str(num)*c, end='')
print()