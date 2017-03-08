#include <iostream>
#include <algorithm>
#include <vector>
#define COLOR int
#define WHITE 0
#define YELLOW 1
#define BLACK 2
using namespace std;
COLOR clr[27];
string s[101];
vector<int> mp[101];
bool flg=true;
int ab[27],ttl;
void dfs(int k)
{
	int i;
	clr[k]=YELLOW;
	for (i=0;i<mp[k].size();i++)
	{
		if (clr[mp[k][i]]==WHITE)
			dfs(mp[k][i]);
		else if (clr[mp[k][i]]==YELLOW)
			flg=false;
	}
	clr[k]=BLACK;
	ab[++ttl]=k;
}
int main()
{
	int n,i,j;
	cin>>n;
	for (i=1;i<=n;i++)
	{
		cin>>s[i];
		if (i==1)
			continue;
		for (j=0;j<s[i].size()&&j<s[i-1].size()&&s[i][j]==s[i-1][j];j++);
		if (j<s[i].size()&&j<s[i-1].size())
			mp[s[i-1][j]-'a'].push_back(s[i][j]-'a');
		else if (s[i-1].size()>s[i].size())
			flg=false;
	}
	for (i=0;i<=25;i++)
		if (clr[i]==WHITE)
			dfs(i);
	if (flg)
		for (i=ttl;i>0;i--)
			cout<<(char)(ab[i]+'a');
	else
		cout<<"Impossible";
	return 0;
}
