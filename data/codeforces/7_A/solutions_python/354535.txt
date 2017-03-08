import fileinput
BCnt = [line.count('B') for line in fileinput.input()]
total = min(BCnt) + BCnt.count(8)
if total == 16:
    print 8
else:
    print total
