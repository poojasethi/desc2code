#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
vector<pair<int,int> > b,c;
int a[32],n,i;

int dfs0(int m,int x,int y,int z)
{
	if(!m) return 0;
	int i,j,t,t1,t2;
	for(i=m;a[i]==a[m];i--);
	if(z&&i+1<m)
	{
		t1=dfs0(i,x,y,0)+m-i+dfs0(i,y,x,0)+m-i+dfs0(i,x,y,1);
		t2=dfs0(n-1,x,6-x-y,0)+1+dfs0(n-1,6-x-y,y,0);
		t=min(t1,t2);
	}
	else t=dfs0(i,x,6-x-y,0)+m-i+dfs0(i,6-x-y,y,0);
	return t;
}

int dfs(int m,int x,int y,int z)
{
	if(!m) return 0;
	int i,j,t,t1,t2;
	for(i=m;a[i]==a[m];i--);
	if(z&&i+1<m)
	{
		t1=dfs0(i,x,y,0)+m-i+dfs0(i,y,x,0)+m-i+dfs0(i,x,y,1);
		t2=dfs0(n-1,x,6-x-y,0)+1+dfs0(n-1,6-x-y,y,0);
		t=min(t1,t2);
		if(t1<t2)
		{
			dfs(i,x,y,0);
			for(j=m;j>i;j--) b.push_back(make_pair(x,6-x-y));
			dfs(i,y,x,0);
			for(j=m;j>i;j--) b.push_back(make_pair(6-x-y,y));
			dfs(i,x,y,1);
		}
		else{
			dfs(n-1,x,6-x-y,0);
			b.push_back(make_pair(x,y));
			dfs(n-1,6-x-y,y,0);
		}
	}
	else{
		t=dfs(i,x,6-x-y,0)+m-i;
		for(j=m;j>i;j--) b.push_back(make_pair(x,y));
		t+=dfs(i,6-x-y,y,0);
		
	}
	return t;
}

int main()
{
	ios::sync_with_stdio(false);
	cin>>n;
	for(i=n;i;i--) cin>>a[i];
	cout<<dfs(n,1,3,1)<<endl;
	for(i=0;i<b.size();i++) cout<<b[i].first<<' '<<b[i].second<<"\n";
	return 0;
}