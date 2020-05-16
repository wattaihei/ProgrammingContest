a, b = map(str, input().split())
X = int(a+b)

ans = 'No'
for x in range(1001):
    if x**2 == X:
        ans = 'Yes'
print(ans)