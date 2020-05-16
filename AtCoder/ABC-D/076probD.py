N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
V.append(0)

prev = 0
ans = 0
for i in range(N):
    at = 0
    if prev < V[i]:
        at = V[i] - prev
    bt = 0
    if V[i] > V[i+1]:
        bt = V[i] - V[i+1]
    if at + bt <= T[i]:
        ans += at**2/2 + at*prev + V[i]*(T[i]-at-bt) + V[i]*bt - bt**2/2
    else:
        a = (T[i]-V[i+1]+prev)/2
        b = (T[i]+V[i+1]-prev)/2
        ans += prev*b + V[i+1]*a + (a**2)/2 + (b**2)/2
    #print(i, ans)
    prev = V[i] - bt

print(ans)