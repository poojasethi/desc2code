#include<iostream>
using namespace std;
int main()
{
string s;
int i,x;
cin>>s;
for(i=1;i<s.length();i++)
{
if(s[i-1]=='r' && s[i]=='u') x=i-1;
}
if(s[0]=='h') cout<<"http://",i=4;
else cout<<"ftp://",i=3;
for(;i<x;i++) cout<<s[i];
cout<<".ru";
if(i+2<s.length())
{
cout<<"/";
for(i=i+2;i<s.length();i++) cout<<s[i];
}
return 0;
}