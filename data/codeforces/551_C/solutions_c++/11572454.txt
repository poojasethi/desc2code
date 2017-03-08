#include <bits/stdc++.h>
using namespace std;
int n,m;
int a[100010],b[100010];
bool check(long long x)
{
	for(int i=1;i<=n;i++) b[i]=a[i];
	int cnt=n;
	long long tmp=0;
	for(int i=1;i<=m;i++)
	{
		while(cnt>0&&b[cnt]==0)
		{
			cnt--;
		}
		if(cnt==0) return true;
		tmp=cnt;
		while(cnt>0&&b[cnt]+tmp<=x)
		{
			tmp+=b[cnt];
			b[cnt]=0;
			cnt--;
		}
		if(cnt==0) return true;
		b[cnt]-=(x-tmp);
	}
	return false;
}
int main()
{
	cin>>n>>m;
	long long sum=n;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i];
		sum+=a[i];
	}
	long long l=0,r=sum,m;
	while(l<r)
	{
		m=(r+l)/2;
		if(check(m)) r=m;
		else l=m+1;
	}
	cout<<l<<endl;
	return 0;
}
