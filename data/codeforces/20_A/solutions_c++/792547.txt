#include <iostream>
 
using namespace std;
 
int main()
{
    string s;
    cin>>s;
    string s2;s2+=s[0];
    for(int c=1;c<s.size();c++)
        if(s[c]!='/'||s[c-1]!='/')
            s2+=s[c];
    for(int c2=s2.size()-1;s2[c2]=='/'&&s2.size()>1&&c2>=0;c2--) s2[c2]=' ';
    cout<<s2;
}