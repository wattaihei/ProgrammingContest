n, r = map(int, input().rstrip().split())
if n >= 10:
    ans = r
else:
    ans = r + 100*(10-n)
print(ans)