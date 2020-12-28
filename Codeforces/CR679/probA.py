import sys
input = sys.stdin.readline
import time 

N = 5*10**7
L = [N-i for i in range(N)]
t0 = time.time()
L.sort()
t1 = time.time()
print(t1-t0)