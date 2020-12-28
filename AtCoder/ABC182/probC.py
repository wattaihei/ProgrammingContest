N = input()

k = len(str(N))

T = [0, 0, 0]
t = 0
for i in range(k):
    s = int(N[i])
    T[s%3] += 1
    t += s

t %= 3
if t == 0:
    ans = 0
elif t == 1:
    if T[1] > 0:
        ans = 1
    elif T[2] > 1:
        ans = 2
    else:
        ans = -1
else:
    if T[2] > 0:
        ans = 1
    elif T[1] > 1:
        ans = 2
    else:
        ans = -1

if ans != -1 and ans >= k:
    ans = -1

print(ans)