n, m, k = map(int, input().split()) # 横に2個
p = list(map(int, input().split()))

delete = {}
for pp in p:
    delete[pp] = False

start = 1
end = k
ans = 0
count = 0
while count != m:
    c = 0
    d = 0
    for pi in p:
        if delete[pi]:
            continue
        if start <= pi <= end:
            delete[pi] = True
            count += 1
            if pi == start:
                d = 1
            c += 1
        else:
            break
    if c == 0:
        start += k
        end += k
        continue
    end += c
    if d == 1:
        start += 1
    ans += 1
print(ans)