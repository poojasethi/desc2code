#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 04 Aug 2015 02:46:39 PM CST
#
#

s=raw_input();
k=input();

mod=1000000007

l=len(s)

q=1;
total=0;

for i in range(l):
    if s[i]=='0' or s[i]=='5':
        total+=q
        total%=mod

    q*=2
    q%=mod

inv = pow(1-q,mod-2,mod)

total=total*(1-pow(q,k,mod))*inv%mod
total+=mod

print total%mod
