n = int(raw_input())
seq1,seq2 = raw_input(),raw_input()
l1,l2 = len(seq1),len(seq2)
lim = l1*l2
arr1,arr2 = [0]*(lim+1),[0]*(lim+1)

for i in xrange(lim):
    c1,c2 = seq1[i%l1],seq2[i%l2]
    arr1[i+1],arr2[i+1] = arr1[i],arr2[i]
    if(c1 == c2): continue;
    if((c1 == 'R' and c2 == 'S') or (c1 == 'S' and c2 =='P') or (c1 =='P' and c2 =='R')):
        arr2[i+1]+=1
    else:
        arr1[i+1]+=1

print arr1[lim]*(n/lim)+arr1[n%lim],arr2[lim]*(n/lim)+arr2[n%lim]
