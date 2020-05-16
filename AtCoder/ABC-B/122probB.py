S = input()
N = len(S)


AGTC = ['A', 'G', 'T', 'C']
part_l = []
for i in range(N):

        if S[i] in AGTC:
                if i == 0:
                        part = [S[i]]
                elif S[i-1] in AGTC:
                        part.append(S[i])
                else:
                        part = [S[i]]
        else:
                if i == 0:
                        part = []
                elif S[i-1] in AGTC:
                        part_l.append(part)
                        part = []
part_l.append(part)

max_part = []          
for part in part_l:
        if len(part) > len(max_part):
                max_part = part

print(len(max_part))