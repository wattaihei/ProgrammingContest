N, R = map(int, input().split())
S = input()

last = -1
for i in range(N):
    if S[i] == ".":
        last = i
if last == -1:
    print(0)
else:
    to_move = max(last - R + 1, 0)
    i = 0
    ans = to_move
    while i <= to_move:
        if S[i] == '.':
            i += R
            ans += 1
        else:
            i += 1
    while i < N:
        if S[i] == ".":
            ans += 1
            break
        i += 1
    print(ans)