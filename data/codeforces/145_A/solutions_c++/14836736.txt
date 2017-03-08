#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s1,s2;
	cin>>s1>>s2;
	long int a = 0,b = 0,i;
	for (i=0;i<s1.size();i++)
	{
		if (s1[i] == '4' && s2[i]=='7')
		a++;
		else if(s1[i]=='7'&&s2[i]=='4')
		b++;
	}
	cout<<max(a,b);
	return 0;
}
