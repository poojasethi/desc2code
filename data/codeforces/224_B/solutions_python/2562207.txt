import sys

n, m = map(int, raw_input().split());
a = map(int, raw_input().split());

flag = [0] * 100003;
for i in xrange(0, 100001):
    flag[i] = 0;
cnt = 0;
ind = -1;
for i, x in enumerate(a):
   # print(x, flag[x]);
    if flag[x] == 0:
        flag[x] = 1;
        cnt = cnt + 1;
    if cnt == m:
        ind = i;
        break;
# print(ind, cnt, m);

end=0;

if ind == -1:
    print('-1 -1');
    end = 1;
if(end == 0):
    for i in xrange(ind, -1, -1):
        x = a[i];
    # print(i, x, flag[x], cnt);
        if flag[x] == 1:
            cnt = cnt - 1;
            flag[x] = 0;
        if cnt == 0:
            print(str(i+1) + ' ' + str(ind+1));
            break;
        
