import numpy as np

A, B, X = map(int, input().split())
if A**2*B/2 > X:
    d = X*2/B/A
    ans = np.arctan(B/d)/np.pi*180
else:
    d = X*2/A/A - B
    ans = np.arctan((B-d)/A)/np.pi*180
print(ans)