
def main():
    import sys
    input = sys.stdin.buffer.readline

    N = int(input())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    has_bag_num = list(map(lambda x:int(x)-1, input().rstrip().split()))

    bag_belongs = [-1]*N
    for person, bag in enumerate(has_bag_num):
        bag_belongs[bag] = person

    R = []
    for i, a in enumerate(A):
        R.append((a, i))

    R.sort()

    ans = []
    for a, person in R:
        bag = has_bag_num[person]
        if bag == person:
            continue
        if B[bag] >= a:
            print(-1)
            return
        person2 = bag_belongs[person]
        if B[person] >= A[person2]:
            print(-1)
            return
        ans.append((person, person2))
        has_bag_num[person] = person
        has_bag_num[person2] = bag
        bag_belongs[person] = person
        bag_belongs[bag] = person2

    print(len(ans))
    for i, j in ans:
        print(i+1, j+1)

if __name__ == "__main__":
    main()