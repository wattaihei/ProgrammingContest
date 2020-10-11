import sys
input = sys.stdin.readline


N = int(input())
S = list(input().rstrip())

one = set()
two = set()
thi = set()
for s in S:
    for t in two:
        thi.add(t+s)
    for o in one:
        two.add(o+s)
    one.add(s)

print(len(thi))