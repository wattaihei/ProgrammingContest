import sys
input = sys.stdin.readline
INF = 10**7

def inout(S):
    print(S)
    sys.stdout.flush()
    num = int(input())
    if num == 0:
        exit(0)
    return num

def main():
    n = inout("a") + 1
    if n == 301:
        inout("b"*300)
    num_b = inout("a"*n)
    if num_b == n:
        inout("b"*(n-1))
    P = []
    for i in range(n-1):
        S = "a"*i + "b" + "a"*(n-1-i)
        P.append(inout(S))

    S = ""
    b = 0
    for p in P:
        if p == num_b-1:
            S += "b"
            b += 1
        else:
            S += "a"
    if b < num_b:
        S += "b"
    else:
        S += "a"
    inout(S)

if __name__ == "__main__":
    main()