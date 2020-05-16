Q = int(input())
Query = []
for _ in range(Q):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    Query.append((a, b, x, y))

for a, b, x, y in Query:
    ans = min([
        (x+y)*a,
        abs(x-y)*a+min(x,y)*b,
        #max(x,y)*b if (x-y)%2 == 0 else (max(x,y)-1)*b+a
    ])
    print(ans)