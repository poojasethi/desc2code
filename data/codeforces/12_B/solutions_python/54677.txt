ques = raw_input()
ans = raw_input()
zeros = ques.count('0')
myans = [x for x in ques if x != '0']
myans.sort()
if ques == '0':
    if ans == '0':
        print 'OK'
    else:
        print 'WRONG_ANSWER'
elif ans == myans[0] + '0' * zeros + ''.join(myans[1:]):
    print 'OK'
else:
    print 'WRONG_ANSWER'
