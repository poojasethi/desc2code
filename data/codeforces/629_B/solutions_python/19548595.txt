n = input()
male = [0] * 367
female = [0] * 367
for _ in xrange(n):
    words = raw_input().split(' ')
    a, b = map(int, words[1:])
    if words[0] == 'M':
        for i in xrange(a, b + 1):
            male[i] += 1
    else:
        for i in xrange(a, b + 1):
            female[i] += 1
max_num = 0
for i in xrange(367):
    max_num = max(max_num, min(male[i], female[i]))
print max_num * 2
