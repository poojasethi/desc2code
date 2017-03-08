T = int(raw_input())

for i in range(T):
    s = raw_input()
    freq = {}
    for ch in s:
        if freq.get(ch, 0) == 0:
            freq[ch] = 1
        else:
            freq[ch] += 1
    
    a = freq.values()
    lena = len(a)
    
    flag = False
    for j in range(lena):
        k=0
        total = 0
        while(k<lena):
            if j!=k:
                total += a[k]
            k += 1
        if a[j] == total:
            flag = True
            break
    print 'YES' if flag else 'NO'
