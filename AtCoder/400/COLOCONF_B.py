S = input()

oper = ['+', '-', '*', '/']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

stack = []
n = ''
for s in S:
    if not s in num and n != '':
        stack.append(n)
        n = ''
    if s == ')':
        p = []
        while True:
            t = stack.pop()
            if t in oper:
                a = t.join(p[::-1])
                break
            else:
                p.append(t)
        stack.append('(' + a + ')')
    elif s in num:
        n += s
    elif s != '(' and s != ',':
        stack.append(s)
if not stack:
    stack.append(n)
print(stack[0])