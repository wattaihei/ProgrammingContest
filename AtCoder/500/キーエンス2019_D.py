import sys
input = sys.stdin.readline
from bisect import bisect_left
from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mod = 10**9+7

A.sort()
B.sort()
dic_A = Counter(A)
dic_B = Counter(B)

ans = 1
for n in reversed(range(1, N*M+1)):
    if n in dic_A.keys() and n in dic_B.keys():
        if dic_A[n] != 1 or dic_B[n] != 1:
            ans = 0
    elif n in dic_A.keys():
        if dic_A[n] != 1:
            ans = 0
        else:
            prob = M - bisect_left(B, n)
            ans = ans * prob % mod
    elif n in dic_B.keys():
        if dic_B[n] != 1:
            ans = 0
        else:
            prob = N - bisect_left(A, n)
            ans = ans * prob % mod
    else:
        prob_A = N - bisect_left(A, n)
        prob_B = M - bisect_left(B, n)
        prob = prob_A * prob_B - (N*M-n)
        ans = ans * prob % mod
print(ans) 
