from sys import stdin
s = raw_input()
stack = []
match = [False] * (len(s) + 1)
for i, c in enumerate(s):
    if c == ')':
        if not stack:
            stack = []
        else:
            l = stack.pop()
            match[l] = True
            match[i] = True
    else:
        stack.append(i)
maxlen = 0 
occr = 1 
prev = -1
for i in range(len(s) + 1): 
    if not match[i]:
        l = i - prev - 1 
        if l > maxlen:
            maxlen = l 
            occr = 1 
        elif l == maxlen and l != 0:
            occr += 1
        prev = i 
print maxlen, occr
