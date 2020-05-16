import sys
input = sys.stdin.readline
import math

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    B = []
    Amax = A[-1]
    for i in range(N-1):
        B.append(Amax-A[i])
    
    R = max(B)
    for b in B:
        if b != 0:
            R = min(R, b)
    
    prob = []
    for n in range(1, int(math.sqrt(R)) + 2):
        #print(n)
        if R%n == 0:
            prob.append(n)
            prob.append(R//n)
    prob.sort(reverse=True)
    #print(R, prob)
    for p in prob:
        ok = True
        for b in B:
            if b%p != 0:
                ok = False
        if ok:
            z = p
            break

    y = 0
    for b in B:
        y += b//z
    print(y, z)

if __name__ == "__main__":
    main()