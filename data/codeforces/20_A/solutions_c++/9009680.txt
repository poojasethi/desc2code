#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s; cin>>s;
	string s2=string(s.size(),'/');
	if(s!=s2){
	for(int i=0;i<s.length();i++)
	{
		if(s[i]=='/'&&(i==s.size()-1||s[i]==s[i+1]))
			s.erase(i,1),i--;
	}
	cout<<s<<endl;}
	else
		cout<<"/\n";
	return 0;
}
