import sys
input = sys.stdin.readline

def convert(S, start):
    hour = int(S[:2])
    minu = int(S[2:])
    m = hour*60 + minu
    if start:
        return m//5
    else:
        return (m+4)//5

N = int(input())
Times = [list(input().rstrip().split("-")) for _ in range(N)]

L = 12*24+2
Imos = [0]*(L+1)
for st, et in Times:
    c_st = convert(st, True)
    c_et = convert(et, False)
    Imos[c_st] += 1
    Imos[c_et] -= 1

for i in range(L):
    Imos[i+1] += Imos[i]

pre = -1
ansArray = []
for t in range(L+1):
    if Imos[t] > 0:
        if pre == -1:
            pre = t
    else:
        if pre >= 0:
            ansArray.append((pre, t-1))
            pre = -1

def decode(s):
    return "{:02}".format(s//12) + "{:02}".format(s%12*5)

for st, et in ansArray:
    print(decode(st) + "-" + decode(et+1))