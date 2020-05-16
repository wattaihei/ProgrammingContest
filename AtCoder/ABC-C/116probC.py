N = int(input())
H = list(map(int, input().split())) # １行に別れてるとき

D = []
for i in range(N-1):
    D.append(H[i+1]-H[i])

ans = 0
up = True
down = False
for i in range(N-2):
    if i == 0 and D[i] < 0:
        ans += H[0]
        up = False
    if (D[i] > 0 and D[i+1] < 0) or (up and D[i+1] < 0):
        ans += H[i+1]
        up = False
    elif D[i] > 0 and D[i+1] == 0:
        up = True
    
    if (D[i] < 0 and D[i+1] > 0) or (down and D[i+1] > 0):
        ans -= H[i+1]
        down = False
    elif D[i] < 0 and D[i+1] == 0:
        down = True
if up or D[-1] > 0:
    ans += H[-1]


print(ans)
