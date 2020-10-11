import sys
input = sys.stdin.buffer.readline

N, X, M = map(int, input().split())

SeqToNum = []
NumToSeq = {}

while not X in NumToSeq:
    NumToSeq[X] = len(SeqToNum)
    SeqToNum.append(X)
    X = X * X % M

if N <= NumToSeq[X]:
    ans = 0
    for i in range(N):
        ans += SeqToNum[i]
else:
    ans = 0
    for i in range(NumToSeq[X]):
        ans += SeqToNum[i]
    N -= NumToSeq[X]
    # cycle
    cycleScore = 0
    cycle = len(NumToSeq) - NumToSeq[X]
    for i in range(NumToSeq[X], len(NumToSeq)):
        cycleScore += SeqToNum[i]
    ans += cycleScore*(N//cycle)
    N %= cycle
    
    for i in range(NumToSeq[X], NumToSeq[X] + N):
        ans += SeqToNum[i]

print(ans)