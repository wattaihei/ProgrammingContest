N = int(input())
A = list(map(int, input().split()))

x = False
k = {}
for i in range(N):
    if not A[i] in k:
        k[A[i]] = 1
    else:
        k[A[i]] += 1
B = 0
a = 0
if len(k.keys()) == 3:
    B = 0
    for key, val in k.items():
        if val == N // 3:
            a += 1
        B = B ^ key
elif len(k.keys()) == 2:
    for key, val in k.items():
        if val == N // 3 and key == 0:
            a += 1
        elif val == N // 3 * 2:
            a += 2
    B = 0
elif len(k.keys()) == 1:
    a = list(k.keys())
    if a[0] == 0:
        x = True

if (N % 3 == 0 and B == 0 and a == 3) or x:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)