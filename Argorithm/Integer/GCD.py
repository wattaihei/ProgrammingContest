
import math
# listのGCD
# O(|A|+√min(A))くらい？
def gcd(A):
    # R = nonzeroの最小
    R = max(A)
    for a in A:
        if a != 0:
            R = min(R, a)
    
    # R の約数全列挙
    prob = []
    for n in range(1, int(math.sqrt(R)) + 2):
        #print(n)
        if R%n == 0:
            prob.append(n)
            prob.append(R//n)
    prob.sort(reverse=True)

    # 大きい方から確認
    for p in prob:
        ok = True
        for a in A:
            if a%p != 0:
                ok = False
        if ok:
            return p

if __name__ == "__main__":
    A = [4, 8, 40]
    print(gcd(A))