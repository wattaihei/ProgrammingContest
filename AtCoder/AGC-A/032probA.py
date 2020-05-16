N = int(input())
b = list(map(int, input().split()))

ans = []
while b:
    
    next = -1
    for i, n in enumerate(b):
        if i + 1 == n:
            next = i
    if next == -1:
        ans = []
        break
    else:
        ans.append(b.pop(next))

if ans:
    ans = ans[::-1]
    for s in ans:
        print(s)
else:
    print(-1)