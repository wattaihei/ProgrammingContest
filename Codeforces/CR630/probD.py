import sys
input = sys.stdin.readline


k = int(input())

a = 1<<(k.bit_length())
print(2, 3)
print(a|k, k, 0)
print(a, a|k, k)