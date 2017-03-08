n = int(raw_input())
text = raw_input();
start = 0;
res = 0;
cur = 0;
flag = True
for  i in range(0, len(text)):
    if text[i] == '!' or text[i] == '?' or text[i] == '.':
        size = i - start + 1
        start = i + 2
        if cur > 0:
            cur += 1
        cur += size
        if cur > n:
            res += 1
            cur = size
            if cur > n:
                if flag:
                    print "Impossible"
                flag = False

if flag:
    if cur > 0:
        print res + 1
    else:
        print res
