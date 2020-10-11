import sys
input = sys.stdin.readline

N = int(input())
A = list(map(str, input().rstrip().split()))

print("Four" if len(set(A))==4 else  "Three")