import sys
input = sys.stdin.buffer.readline

def primes(M):
    most = [-1]*(M+1)
    for m in range(2, M+1):
        if most[m] == -1:
            most[m] = 1
            l = 2
            while m*l <= M:
                most[m*l] = m
                l += 1
    return most

def main():
    N = int(input())
    A = list(map(int, input().split()))
    most = primes(max(A))
    for a in A:
        