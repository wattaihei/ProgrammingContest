N, M = map(int, input().split()) # 横に2個

for i in range(N):
    ob = set(list(map(int, input().split()))[1:])
    if i == 0:
        ans = ob
    else:
        ans = ans & ob

print(len(ans))