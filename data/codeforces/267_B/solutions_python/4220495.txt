mmarr = [[0 for i in range(7)] for i in range(7)]
mmn = [0 for i in range(7)]
mmin = []
#print mmarr
found = 0
n =0
rarr = []
def print_res():
    global rarr
    global mmin
    #print mmin
    l = len(mmin)
    for i in range(l):
        #print rarr[i]
        for j in range(l):
            if rarr[i][0] == mmin[j][0] and rarr[i][1] == mmin[j][1] and mmin[j][2] == 0:
                print str(j+1) + " +"
                mmin[j][2] = 1
                break
            elif rarr[i][0] == mmin[j][1] and rarr[i][1] == mmin[j][0] and mmin[j][2] == 0:
                print str(j+1) + " -"
                mmin[j][2] = 1
                break
        #print mmin
def dfs(s,cnt):
    global found
   # print rarr
    if found == 1:
        return
    if cnt == n:
        #print "found"
        found = 1
        #print rarr
        print_res()
    for i in range(7):
        if mmarr[s][i] > 0:
            mmarr[s][i]-=1
#            if i !=s:
            mmarr[i][s]-=1
#            print mmarr
            rarr.append([s,i])
            dfs(i,cnt+1)
            mmarr[s][i]+=1
#            if i !=s:
            mmarr[i][s]-=1
            rarr.pop()
n = int(raw_input())
for i in range(n):
    a,b = map(int,raw_input().split())
    mmin.append([a,b,0]);
    mmn[a]+=1
    mmn[b]+=1
    mmarr[a][b]+=1
    mmarr[b][a]+=1
'''
print mmn

for mm in mmarr:
    print mm
'''
s = 0
ocnt = 0
for i in range(7):
    if mmn[i]>0:
        s = i
    #print mmn[i] & 1
    if (mmn[i] & 1) == 1:
        ocnt+=1
        s = i
#print "start",s
if ocnt > 2:
    print "No solution"
else:
    if ocnt > 0:
        for i in range(7):
            if mmn[i] & 1 ==1 and found == 0:
                #print "do ",i
                dfs(i,0)
    else:
         for i in range(7):
            #print mmn[i]
            if mmn[i]>0 and found == 0:
                #print "do ",i
                dfs(i,0)
    if found ==0:
        print "No solution"
