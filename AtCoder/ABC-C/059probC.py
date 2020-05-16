N = int(input())
A = list(map(int, input().split()))

def count(s):
    ans = 0
    for i, a in enumerate(A):
        if i == 0:
            continue
        if s < 0:
            if 1-s-a >= 0:
                ans += 1-s-a
                s = 1
            else:
                s += a
        elif s > 0:
            if s+a+1 >= 0:
                ans += s+a+1
                s = -1
            else:
                s += a
    return ans

b = A[0]
ans1 = count(b)
if b > 0:
    ans2 = count(-1)+b+1
elif b < 0:
    ans2 = count(1)+1-b
else:
    ans1 = count(1)+1
    ans2 = count(-1)+1
print(min(ans1, ans2))