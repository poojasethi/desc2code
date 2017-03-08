#include<iostream>
using namespace std;
int main()
{
string s="qwertyuiopasdfghjkl;zxcvbnm,./",a,b;
cin>>a>>b;
for(int i=0; i<b.size(); i++)
cout<<s[s.find(b[i])-(a=="R")+(a=="L")];
return 0;
}