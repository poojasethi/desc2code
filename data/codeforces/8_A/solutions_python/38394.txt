from re import match
flags = raw_input()
p1 = raw_input()
p2 = raw_input()
pattern = '.*' + p1 + '.*' + p2 + '.*'
forward = match(pattern, flags) is not None
backward = match(pattern, flags[::-1]) is not None
if forward and backward:
    print 'both'
elif forward:
    print 'forward'
elif backward:
    print 'backward'
else:
    print 'fantasy'
