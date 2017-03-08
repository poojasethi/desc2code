#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long i,m=0,ans=0;
    string s;
    cin>>s;
    for(i=0;i+4<s.size();i++){
        string str=s.substr(i,5);
        if(str=="heavy")
            m++;
        if(str=="metal") ans+=m;
    }
    cout<<ans<<endl;
}
