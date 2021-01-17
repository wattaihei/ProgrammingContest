import sys
input = sys.stdin.readline

H = 18
W = 6
state = [list("0"+input().rstrip()+"0") for _ in range(H)]

state = [list("0"*(W+2))] + state + [list("0"*(W+2))]

dp = [[[0]*(1<<W) for _ in range(1<<W)] for _ in range(H+2)]

def match(bit, h):
    for w in range(W):
        if state[h+1][w+1] == "?": continue
        if str((bit>>w)&1) != state[h+1][w+1]: return False
    return True

def allowed(bit, pbit, qbit):
    for w in range(W):
        L = [
            (pbit>>w)&1,
            (pbit>>(w-1))&1 if w > 0 else 0,
            (pbit>>(w+1))&1 if w < W-1 else 0,
            (bit>>w)&1,
            (qbit>>w)&1
        ]
        L.sort()
        if L[2] != (pbit>>w)&1:
            return False
    return True

for bit in range(1<<W):
    dp[0][bit][0] = 1

for i in range(1,H+1):
    for bit in range(1<<W):
        if not match(bit, i): continue
        for pbit in range(1<<W):
            if not match(pbit, i-1): continue
            for qbit in range(1<<W):
                if not match(qbit, i-2): continue
                if allowed(bit, pbit, qbit):
                    dp[i][bit][pbit] += dp[i-1][pbit][qbit]

ans = 0
for bit in range(1<<W):
    ans += dp[H][0][bit]

print(ans)