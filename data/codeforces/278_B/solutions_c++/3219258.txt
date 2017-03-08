#include<iostream>
#include<cstring>
using namespace std;
int n,nr[2][700];

int main()
{
	int i,j,sz;
	string cuv;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>cuv;
		sz=cuv.size();
		for(j=0;j<sz;j++)
		{
			nr[0][cuv[j]-'a']++;
			if(j<sz-1)
				nr[1][(cuv[j]-'a')*26+cuv[j+1]-'a']++;
		}
	}
	for(j=0;j<26;j++)
		if(nr[0][j]==0)
		{
			cout<<(char)(j+'a')<<"\n";
			return 0;
		}
	for(j=0;j<26*26;j++)
		if(nr[1][j]==0)
		{
			cout<<(char)(j/26+'a')<<(char)(j%26+'a')<<"\n";
			return 0;
		}
	return 0;
}
