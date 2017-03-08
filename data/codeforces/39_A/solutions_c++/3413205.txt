#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int b[10000],a,n,i,j,k,ans;
string s;
int main()
{
    cin>>a>>s;
    if(s[0]!='-') s="+"+s;
    for(i=0;i<s.length();i+=3)
    {
        k=s[i++]=='+'?1:-1;
        for(j=0;s[i]>='0'&&s[i]<='9';i++) j=j*10+s[i]-'0';
        if(s[i]=='*') i++; else j=1;
        b[++n]=(j*=k);
        ans+=(a-(s[i]=='a'))*j;
    }
    sort(b+1,b+n+1);
    for(i=1;i<=n;i++) ans+=i*b[i];
    cout<<ans<<endl;
    return 0;
}