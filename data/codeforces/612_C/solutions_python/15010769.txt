import sys

def judge(x):
    m = {'<':'>', '{':'}', '[':']', '(':')'}
    stack = []
    count = 0
    for ch in x:
        if ch in ['>', '}', ']', ')']:
            if len(stack) == 0:
                return -1
            if m[stack[-1]] != ch:
                count += 1
            stack.pop()
        else:
            stack.append(ch)
    if len(stack) > 0:
        return -1
    else:
        return count

get = sys.stdin.readline().strip()
out = judge(get)
if out > -1:
    print out
else:
    print "Impossible"
