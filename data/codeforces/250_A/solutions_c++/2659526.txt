#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int main(){
int flag=0,count=0,i=0,ans=0,n,a;
vector<int>ar;
cin>>n;
while(n--){
cin>>a;
if(a<0){
flag++;
}
if(flag<3)
count++;
else{
ans++;
flag=1;
ar.push_back(count);
count=1;
}
}
printf("%d\n",ans+1);
for(i=0;i<ar.size();i++)
printf("%d ",ar[i]);
printf("%d",count);
}
