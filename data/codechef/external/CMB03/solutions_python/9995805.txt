a = input()
for x in range(a):
    test = raw_input().split()
    if test[1] in test[0]:
        print 1
    else:
        print 0