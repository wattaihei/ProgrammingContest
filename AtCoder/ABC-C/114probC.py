N = input()
L = len(N)
NUM = int(N)

count = 0
for l in range(1, L):
        count += 3**l - 3*2**l + 3
q = '3'*L
while True:
        if int(q) > NUM:
                break
        if q.count('3') > 0 and q.count('5') > 0 and q.count('7') > 0:
                count += 1
        if q == '7'*(L-2) + '5' + '3':
                break
        for i in range(1, L+1):
                k = q[-i]
                if k == '3':
                        next = q[:-i] + '5' + '3'*(i-1)
                        break
                elif k == '5':
                        next = q[:-i] + '7' + '3'*(i-1)
                        break
        q = next

print(count)