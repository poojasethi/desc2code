#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		int n;
		cin>>n;
		vector<int> vec;
		vec.resize(n);
		for(int i=0;i<n;i++)
		{
			cin>>vec[i];
		}
		sort(vec.begin(),vec.end());
		int ans=1000000000;
		for(int i=1;i<n;i++)
		{
			if(vec[i]-vec[i-1]<ans)ans=vec[i]-vec[i-1];
		}
		cout<<ans<<endl;
	}
}