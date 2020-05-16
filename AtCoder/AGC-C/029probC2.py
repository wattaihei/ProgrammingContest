import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


def check(m):
    if m == 1:
        pre = -1
        for a in A:
            if pre >= a:
                return False
            pre = a
    else:
        dp = {}
        pre = 0
        #count = 0
        for a in A:
            if pre < a:
                pre = a
                continue
            todelete = []
            for b in dp.keys():
                if b > a:
                    todelete.append(b)
            ind = a
            while ind > 0:
                if ind in dp and dp[ind] >= m-1:
                    todelete.append(ind)
                else:
                    break
                ind -= 1
            # 更新
            if ind in dp:
                dp[ind] += 1
            else:
                dp[ind] = 1
            if ind == 0 or dp[ind] >= m:
                return False
            for d in todelete:
                del dp[d]
            pre = a
    #print(m, count)
    return True



def main():
    l = 0
    r = N
    while r-l > 1:
        m = (r+l)//2
        if check(m):
            r = m
        else:
            l = m
    print(r)


if __name__ == "__main__":
    main()
