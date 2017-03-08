#include <iostream>
#include<string>
using namespace std;

int main()
{
   string s;
   int n,d[27]={},i,j,l,k;
   cin>>n>>s;
   for(i=0;i<s.size();i++)
   {
       d[s[i]-'a']++;
   }
   for(i=0;i<26;i++)
   {
       if(d[i]%n!=0) {cout<<-1;return 0;}
   }
   for(i=0;i<n;i++)
   {
       for(l=0;l<26;l++)
       for(j=0;j<d[l]/n;j++)
       cout<<(char)(l+97);
   }
    return 0;
}