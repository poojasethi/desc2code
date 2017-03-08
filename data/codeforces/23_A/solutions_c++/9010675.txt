#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s; cin>>s;
	map<string,int>m;
	int mx=0;
	for(int i=0;i<s.length();i++)
	{
		for(int j=1;j<=s.length()-i;j++)
		{
			string str=s.substr(i,j);
			m[str]+=1;
			if(m[str]>1)
				mx=max(mx,int(str.size()));
		}
	}
	cout<<mx<<endl;

	return 0;
}
