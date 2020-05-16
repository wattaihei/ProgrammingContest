import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

bit = 1
for a in A:
    bit |= (bit<<a)

S = sum(A)
for i in range((S+1)//2, S+1):
    if bit&(1<<i):
        print(i)
        break