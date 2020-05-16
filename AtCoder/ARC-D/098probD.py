N = int(input())
A = list(map(int, input().split()))

# 2進数変換
A2 = []
for a in A:
    a1 = a
    ans = []
    while a1 > 0:
        a1, a2 = a1//2, a1%2
        ans.append(a2)
    A2.append(ans)

# しゃくとり
ans = 0
start = 0 
end = 0
startup = False
while True:
    print(start, end)
    checked = [False for _ in range(20)]
    lose = False
    for a in A2[start:end+1]:
        print(a)
        for i, num in enumerate(a):
            if num == 1:
                if checked[i]:
                    lose = True
                    break
                checked[i] = True
        if lose:
            break
    if startup:
        if not lose:
            ans += 1
        if start == end:
            if start == N-1:
                break
            end += 1
            startup = False
        else:
            start += 1
    elif lose:
        start += 1
        startup = True
    elif end == N - 1:
        ans += 1
        start += 1
        startup = True
    else:
        ans += end - start + 1
        end += 1
        startup = False
    print(ans)


print(ans)
