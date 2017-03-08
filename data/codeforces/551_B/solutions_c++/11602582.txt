#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int t[30],ta[30],tb[30],ansa=0,ansb=0;
int main()
{
string s,a,b;
cin>>s>>a>>b;
for(int i=0;i<s.size();i++)
	t[s[i]-'a']++;
for(int i=0;i<a.size();i++)
	ta[a[i]-'a']++;
for(int i=0;i<b.size();i++)
	tb[b[i]-'a']++;
int sum=1000000;
for(int i=0;i<26;i++)
	if(ta[i])
		sum=min(sum,t[i]/ta[i]);
for(int i=0;i<=sum;i++){
	int res=1000000;
	for(int j=0;j<26;j++)
		if(tb[j])
		res=min(res,(t[j]-ta[j]*i)/tb[j]);
	if(i+res>ansa+ansb)ansa=i,ansb=res;
}
for(int i=0;i<ansa;i++)
cout<<a;
for(int i=0;i<ansb;i++)
cout<<b;
for(int i=0;i<26;i++)
	for(int j=0;j<t[i]-ta[i]*ansa-tb[i]*ansb;j++)
	cout<<char(i+'a');
}
