import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ok = True
for a in A:
    if a%2 == 0:
        if a%5 != 0 and a%3 != 0:
            ok = False
print("APPROVED" if ok else "DENIED")