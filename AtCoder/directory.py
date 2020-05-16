import os
import shutil

probs = ['probA.py', 'probB.py', 'probC.py', 'probD.py', 'probE.py', 'probF.py']

for a in range(111, 134):
    dirname = 'ABC' + str(a)
    for prob in probs:
        filename = dirname + '/' + prob
        now = prob[4]
        if os.path.exists(filename):
            newname = dirname + '/' + str(a) + prob
            os.rename(filename, newname)
            shutil.move(newname, 'ABC-' + now)
    if not os.listdir(dirname):
        os.rmdir(dirname)

