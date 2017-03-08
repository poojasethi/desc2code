#include <bits/stdc++.h>

using namespace std;


class order
{
public:
	int a,b,d;
};


bool comp(order p, order q)
{
	if(p.d<q.d)return true;
	return false;
}

int main()
{
	int n,x,y;
	cin>>n>>x>>y;
	vector<order> vec;
	vec.resize(n);
	for(int i=0;i<n;i++)
	{
		cin>>vec[i].a;
	}
	for(int i=0;i<n;i++)
	{
		cin>>vec[i].b;
		vec[i].d=abs(vec[i].a-vec[i].b);
	}
	sort(vec.begin(),vec.end(),comp);
	int ans=0;
	for(int i=n-1;i>=0;i--)
	{
		if(x>0&&y>0)
		{
			if(vec[i].a>=vec[i].b)
			{
				ans+=vec[i].a;
				x--;
			}
			else if(vec[i].b>vec[i].a)
			{
				ans+=vec[i].b;
				y--;
			}
		}
		else if(x>0)
		{
			ans+=vec[i].a;
			x--;
		}
		else
		{
			ans+=vec[i].b;
			y--;
		}
	}
	cout<<ans<<endl;

}