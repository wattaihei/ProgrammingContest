
ans = 0
for n in range(1, 101):
    if n%3 != 0 and n%5 != 0:
        ans += n
print(ans)