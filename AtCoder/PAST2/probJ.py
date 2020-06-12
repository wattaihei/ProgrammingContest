import sys
input = sys.stdin.readline

S = input().rstrip()

stack = [""]
for s in S:
    if s == "(":
        stack.append("")
    elif s == ")":
        t = stack.pop()
        c = stack.pop()
        stack.append(c+t+t[::-1])
    else:
        stack[-1] += s

print(stack[0])