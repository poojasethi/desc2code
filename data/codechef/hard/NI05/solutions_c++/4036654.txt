#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;

int main(){
int reward[][10]={
{55,60	,4	,25	,18	,10	,12	,8	,11	,50},
{60	,45	,75	,23	,27	,20	,24	,7	,33	,12},
{4	,75	,78	,32	,36	,30	,36	,6	,12	,65},
{25	,23	,32	,15	,45	,40	,48	,5	,14	,23},
{18	,27	,36	,45	,54	,50	,60	,4	,15	,12},
{10	,20	,30	,40	,50	,60	,72	,3	,32	,34},
{12	,24	,36	,48	,60	,72	,84	,2	,23	,34},
{8	,7	,6	,5	,4	,3	,2	,1	,34	,123},
{11	,33	,12	,14	,15	,32	,23	,34	,65	,48},
{50	,12	,65	,23	,12	,34	,34	,123,48	,71}
};
int t,temp,arr[12];
scanf("%d",&t);
while(t--){
for(int i=0;i<10;i++)scanf("%d",&temp);
for(int i=0;i<10;i++)scanf("%d",&arr[i]);
string s="";
for(int i=0;i<10;i++)
if(arr[i]==1)
s+=(char)i;
int ans=-1;
string os=s;
do{
int tans=0;
for(int i=0;i<os.length();i++)
{
tans+=reward[(int)os[i]][(int)s[i]];
}
ans=max(ans,tans);
}while(next_permutation(s.begin(),s.end()));
printf("%d\n",ans);
}
}
