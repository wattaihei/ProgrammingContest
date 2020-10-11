import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))

used = [False]*(4*10**5)
num = 0
for a in A:
    used[a] = True
    while used[num]:
        num += 1
    print(num)