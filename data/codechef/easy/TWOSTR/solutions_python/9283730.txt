T = int(raw_input())

for i in range(T):
    s1 = raw_input()
    s2 = raw_input()
    flag = True
    for j in range(len(s1)):
        if not (s1[j] == '?' or s2[j] == '?') and (s1[j] != s2[j]):
            flag = False
            break
    print 'Yes' if flag else 'No'
