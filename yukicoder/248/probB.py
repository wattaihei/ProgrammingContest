import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

dic = {}
for i, a in enumerate(A):
    if a in dic:
        dic[a].append(i)
    else:
        dic[a] = [i]

ans = 0
for num, List in dic.items():
    for i in range(len(List)-1):
        if List[i] + 1 != List[i+1]:
            if num == A[0] and num == A[-1] and ans == 0:
                ans = 1
            else:
                ans = -1
print(ans)