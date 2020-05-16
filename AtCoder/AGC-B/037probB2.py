import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

mod = 998244353

have = [0]*8
target_bit = 1

ans = 1

for s in S:
    if s == "R":
        bit = 1
    elif s == "G":
        bit = 2
    else:
        bit = 4
    update = False
    for bit2 in [3, 5, 6]:
        if have[bit2] > 0 and ((bit2&bit) == 0):
            if bit != target_bit:
                ans = ans * have[bit2] % mod
            have[bit2] -= 1
            update = True
    if update:
        continue
    for bit1 in [1, 2, 4]:
        if have[bit1] > 0 and ((bit1&bit) == 0):
            if bit != target_bit:
                if (target_bit&bit1) == 0:
                    ans = ans * (have[bit1|bit]+1) % mod
                else:
                    ans = ans * have[bit1] % mod
            have[bit1] -= 1
            have[bit1|bit] += 1
            update = True
    if update:
        continue
    
    if bit != target_bit:
        ans = ans * (have[bit] + 1) % mod
    have[bit] += 1


for n in range(1, N+1):
    ans = ans * n % mod

print(ans)
