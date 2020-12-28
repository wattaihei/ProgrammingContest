from math import sqrt

def main():
    N = int(input())

    ans =set()
    for n in range(1, int(sqrt(N))+4):
        if N%n == 0:
            ans.add(n)
            ans.add(N//n)

    A = list(ans)
    A.sort()
    print("\n".join(map(str, A)))

if __name__ == "__main__":
    main()