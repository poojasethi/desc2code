
import copy

n, k = map(int, raw_input().split())
number = raw_input()
num = map(int, list(number))

d = dict()
idx = dict()

for i in xrange(n):
    nm = num[i]
    if d.has_key(nm) :
        d[nm] += 1
        idx[nm].append(i)
    else:
        d[nm] = 1
        idx[nm] = [i]

ans_cost = 9999999
ans_number = number

#print n, k, number
#print d
#print idx

for key, value in d.iteritems():
    cnt = value
    cost = 0
    tmp = list(num)
    iid = copy.deepcopy(idx)
    #print "iid=", iid

    if cnt >= k:
        ans_cost = cost
        ans_number = number
        break

    ok = False

    for diff in xrange(1,10):
        if key + diff <= 9 and iid.has_key(key + diff):
            next_key = key + diff
            for next_idx in iid[next_key] :
                cost += diff
                tmp[next_idx] = key
                cnt += 1
                if cnt >= k:
                    ok = True
                    break
        if ok :
            break

        if key - diff >= 0 and iid.has_key(key - diff):
            next_key = key - diff
            for next_idx in iid[next_key][::-1] :
                cost += diff
                tmp[next_idx] = key
                cnt += 1
                if cnt >= k:
                    ok = True
                    break
        
        if ok :
            break

    #print "ok =", ok
    #print "cnt =", cnt
    if ans_cost > cost:
        ans_cost = cost
        ans_number = ''.join(map(str, tmp))
    elif ans_cost == cost :
        ans_number = min(ans_number, ''.join(map(str, tmp)))

print ans_cost
print ans_number
        
              
