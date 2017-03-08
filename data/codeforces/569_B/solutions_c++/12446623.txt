#include<iostream>
#include<map>
using namespace std;
map <int,int>book,vis;
int n;
int s[10000000];
int main()
{
	cin>>n;
	for(int i=1;i<=n;i++) cin>>s[i],book[s[i]]=1;
	int cnt=1;
	for(int i=1;i<=n;i++)
	{
		if(vis[s[i]]==0&&s[i]<=n) {vis[s[i]]=1;continue;}
		while(book[cnt]) cnt++;	
		book[cnt]=1;
		s[i]=cnt;
	}
	for(int i=1;i<=n;i++)
		cout<<s[i]<<" ";
}
