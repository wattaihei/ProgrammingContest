import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

ones = S.count("n")
zeros = S.count("z")
ans = ["1"]*ones + ["0"]*zeros
print(" ".join(ans))