import sys
input = sys.stdin.readline


AT = list(map(int, input().split()))
N = int(input())
A = [int(input()) for _ in range(N)]

US = [None]*10
for i, n in enumerate(AT):
    US[n] = i

def to_us(num):
    strN = str(num)
    S = ""
    for s in strN:
        S += str(US[int(s)])
    return int(S)

def to_at(num):
    strN = str(num)
    S = ""
    for s in strN:
        S += str(AT[int(s)])
    return int(S)

U = []
for a in A:
    U.append(to_us(a))

U.sort()
for u in U:
    print(to_at(u))