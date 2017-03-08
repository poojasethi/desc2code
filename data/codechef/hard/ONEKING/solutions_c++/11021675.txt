#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class boundry
{
public:
	int type,coord,kngdom_no;
};


bool comp(boundry p, boundry q)
{
	if(p.coord<q.coord)return true;
	if(p.coord==q.coord&&p.type<q.type)return true;
	return false;
}

int main()
{
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		int n,temp;
		cin>>n;
		vector<boundry> vec;
		vec.resize(2*n);
		for(int i=0;i<2*n;i++)
		{
			cin>>temp;
			vec[i].coord=temp;
			if(i%2==0)vec[i].type=0;
			else vec[i].type=1;
			vec[i].kngdom_no=i/2;
		}
		sort(vec.begin(),vec.end(),comp);
		int ans=0;
		vector<int> kingdoms,dest;
		dest.resize(2*n);
		for(int i=0;i<vec.size();i++)
		{
			if(vec[i].type==0)kingdoms.push_back(vec[i].kngdom_no);
			else if(vec[i].type==1)
			{
				if(!dest[vec[i].kngdom_no])
				{
					for(int j=0;j<kingdoms.size();j++)
					{
						dest[kingdoms[j]]=1;
					}
					ans++;
					kingdoms.resize(0);
				}
			}
		}
		cout<<ans<<endl;
	}

}