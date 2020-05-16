# -*- coding: utf-8 -*-
from itertools import accumulate
def inpl(): return map(int, input().split())

N = int(input())
A = list(inpl())
l = 0
r = 0
S = 0
ans = 0

while l < N and r < N:
    while r < N:
        print(l, r)
        if S + A[r] == S ^ A[r]: # 合計が条件を満たすなら右に伸ばす
            S += A[r] 
            ans += (r-l+1) 
            r += 1
        else:
            break
    if r > l: # やりきってもまだlが進めるならlを進める
        S -= A[l]
        l += 1
        
    else: # 追いついていたら右に進む
        r += 1
        l += 1

print(ans)
