#include<bits/stdc++.h>
using namespace std;
int n,r;
template<typename __ll>
inline void read(__ll &m)
{
    __ll x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    m=x*f;
}
vector<pair<int,int> > v;
vector<pair<int,int> > ans;
vector<pair<int,int> > aaa;
long long maxx=-999;
void dfs(int k,int d)
{
	int i,j;
	if(d==n)
	{
		int sum=0;
		for(i=0;i<ans.size();i++) 
			for(j=i+1;j<ans.size();j++)
			{
				int xx=ans[i].first;
				int yy=ans[i].second;
				int a=ans[j].first;
				int b=ans[j].second;
				sum+=(xx-a)*(xx-a)+(yy-b)*(yy-b);
			}
		if(maxx<sum)
		{
			aaa=ans;
			maxx=sum;
		} 
		return ;
	}
	for(i=k;i<v.size()&&i<30-2*n;i++)
	{
		ans.push_back(v[i]);
		dfs(i,d+1);
		ans.pop_back();
	}
}
int cmp(pair<int,int> a,pair<int,int> b)
{
	int x=a.first*a.first+a.second*a.second;
	int y=b.first*b.first+b.second*b.second;
	return x>y;
}
int main()
{
	int i,j;
	read(n);
	read(r);
	for(i=-r;i<=r;i++)
		for(j=-r;j<=r;j++)
		{
			int t=i*i+j*j;
			if(t<=r*r&&t>=(r-1)*(r-1))
				v.push_back(make_pair(i,j));
		}
	sort(v.begin(),v.end(),cmp);
	dfs(0,0);
	cout<<maxx<<endl;
	for(i=0;i<aaa.size();i++)
		cout<<aaa[i].first<<" "<<aaa[i].second<<endl;
}