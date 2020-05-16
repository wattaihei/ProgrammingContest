N = int(input())
Query = [list(map(str, input().split())) for _ in range(N)]

stack = [1]
ok = True
ans = 0
for A in Query:
    if A[0] == 'for':
        num = stack[-1]*int(A[1])
        if num > 2**32-1 or stack[-1] == -1:
            stack.append(-1)
        else:
            stack.append(num)
    elif A[0] == 'add':
        if stack[-1] == -1:
            ok = False
            break
        ans += stack[-1]
    else:
        stack.pop()

if ok and ans <= 2**32-1:
    print(ans)
else:
    print("OVERFLOW!!!")