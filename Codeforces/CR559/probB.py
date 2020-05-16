import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    K = 10**14
    for i, a in enumerate(A):
        K = min(a//(max(i, N-i-1)), K)

    print(K)

if __name__ == "__main__":
    main()