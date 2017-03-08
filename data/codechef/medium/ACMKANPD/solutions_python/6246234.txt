#include<iostream>
#include<bitset>
#include<sstream>
using namespace std;
int main()
{
    string s,t;
    while(cin>>t&&t!="~")
    {
        s=t;
        while(cin>>t&&t!="#")
        if(t[0]!='"')s+=' '+t;
        else s+=' '+t.substr(17);
        istringstream in(s);
        int f;
        string bit;
        while(in>>t)
        if(t.size()==1)f=1;
        else if(t.size()==2)f=0;
        else for(int i=0;i<t.size()-2;i++)bit+=char(f+48);
        cout<<bitset<32>(bit).to_ulong()<<endl;
    }
    return 0;
}
