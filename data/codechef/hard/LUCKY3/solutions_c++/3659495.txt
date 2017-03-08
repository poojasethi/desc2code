#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

typedef long long int ll;
using namespace std;

map<pair<int,int>,int> mk;
int lucky[1300];
int a[55];
int q_list[55];
ll dp[55][1<<10];
ll ten[100];
int cc[1100][55];

void generate(void)
{
	int i,j,q,n;
	lucky[1]=4;
	lucky[2]=7;
	j=3;
	ll k=1;
	for(n=2;n<=9;n++)
	{
		for(i=1;i<=(1<<(n-1));i++)
		{
			q=4*ten[n-1]+lucky[k];
			lucky[j++]=q;
			q=7*ten[n-1]+lucky[k];
			lucky[j++]=q;
			k++;
		}
	}
	sort(lucky+1,lucky+1023);
}

inline bool check(int a,int b)
{
	int d_a,d_b;
	while(a && b)
	{
		d_a=a%10;
		a/=10;
		d_b=b%10;
		b/=10;
		if(d_b>d_a)	return false;
	}
	return true;
}

inline int take(int a,int b)
{
	int d,d_n,ans=0,i=0;
	while(b)
	{
		d_n=a%10;
		a=a/10;
		d=b%10;
		b=b/10;
		if(d==d_n)
			ans=ans|(1<<i);
		i++;
	}
	return ans;
}

int main()
{
	int test,i,j,q,w,x,y,k,number;
	ll ans;
	ten[0]=1;
	for(i=1;i<=9;i++)	ten[i]=ten[i-1]*10;
	generate();
	scanf("%d",&test);
	while(test--)
	{
		scanf("%d",&w);
		ans=0;
		int m=-1;
		for(i=0;i<w;i++)	
		{
			scanf("%d",&a[i]);
			if(a[i]>m)	m=a[i];
		}
		int c=0;
		while(m)
		{
			m=m/10;
			c++;
		}
		for(i=1;i<=1022;i++)
		{
			for(j=0;j<w;j++)
				cc[i][j]=take(lucky[i],a[j]);
		}
		for(i=1;i<=1022;i++)
		{
			//if(lucky[i]>m)	continue;
			number=lucky[i];
			j=0;
			int n=number;
			while(n)
			{
				n/=10;
				j++;
			}
			int v=0;
			if(j>c)	continue;
			for(k=0;k<w;k++)
			{
				if(a[k]>number)	continue;
				if(check(number,a[k]))
					q_list[v++]=k;
			}
			for(x=0;x<=v;x++)
				for(y=0;y<(1<<j);y++)	dp[x][y]=0;
			dp[0][0]=1;
			for(x=0;x<v;x++)
			{
				for(y=0;y<(1<<j);y++)
				{
					dp[x+1][y]+=dp[x][y];
					q=cc[i][q_list[x]];
					dp[x+1][y|q]+=dp[x][y];
				}
			}
			ans+=dp[x][(1<<j)-1];
		}
		printf("%lld\n",ans);
	}
	return 0;
}