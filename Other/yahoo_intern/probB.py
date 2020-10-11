import sys
input = sys.stdin.readline

N = int(input())
A = [input().rstrip() for _ in range(N)]

stack = [0]
for a in A:
    if a == "add":
        stack[-1] += 1
    elif a == "print":
        print(stack[-1])
    elif a == "pin":
        t = stack[-1]
        stack.append(t)
    else:
        stack.pop()