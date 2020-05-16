import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

dic = {}
for a in A:
    if not a in dic.keys():
        dic[a] = 1
    else:
        dic[a] += 1

L = []
R = []
for n in range(1, N+1):
    if not n in dic.keys():
        L.append(n)
        continue
    if dic[n] > 1:
        R.append(n)

if len(L) == 0 and len(R) == 0:
    print("Correct")
else:
    print(R[0], L[0])