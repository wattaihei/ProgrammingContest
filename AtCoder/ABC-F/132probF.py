N, K = map(int, input().split()) # 横に2個

ans = 0
root = []
for i in range(1, N+1):
    ans += (N // i) ** (K-1)
    root.append(N//i)
    if i**2 > N:
        next = i
        break

print(root)
for i, r in enumerate(root):
    if i == 0:
        continue
    ans += (i+1) ** (K-1) * (r - N//i)


ans = int(ans % (1E9+7))
print(ans)