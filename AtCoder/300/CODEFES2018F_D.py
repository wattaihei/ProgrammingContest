S = list(input())

ans = 0
mins = 'z'
for s in S:
    if s <= mins:
        ans += 1
        mins = s
print(ans)