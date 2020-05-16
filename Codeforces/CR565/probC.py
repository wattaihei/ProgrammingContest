import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    nums = [4, 8, 15, 16, 23, 42]

    count = {}
    for num in nums:
        count[num] = 0

    for a in A:
        if a in nums:
            if a == 4:
                count[a] += 1
            else:
                ind = nums.index(a)
                prem = nums[ind-1]
                if count[prem] > count[a]:
                    count[a] += 1

    M = count[42]
    ans = N - M*6

    print(ans)

if __name__ == "__main__":
    main()