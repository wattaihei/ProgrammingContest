import math

N = int(input())
mod = int(1E9+7)

def prime(n):
    factor = []
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    if n != 1:
        factor.append(n)
    return factor

def main():
    P = [0 for _ in range(N+1)]
    for n in range(2, N+1):
        A = prime(n)
        for a in A:
            P[a] += 1

    ans = 1
    for p in P:
        ans =  ans * (p+1) % mod

    print(ans)

if __name__ == "__main__":
    main()