N = int(input())

d = 0
ans = 'No'
while d*7 <= N:
    if (N-d*7)%4 == 0:
        ans = 'Yes'
        break
    d += 1

print(ans)