#include<bits/stdc++.h>
using namespace std;
char str[50000];
int res,l,i,j,res2;

int main()
{
    cin>>str;
    l=strlen(str);

    for(i=0;i<l-3;i++)
    if(str[i]=='b' && str[i+1]=='e'&& str[i+2]=='a' &&str[i+3]=='r')
    res+=(((i+1)-j)*(l-(i+3))),j=(i+1);
    cout<<res<<endl;
}
